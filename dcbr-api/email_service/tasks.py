import datetime
import logging
import os
import tempfile

import pytz
import requests
from background_task import background
from background_task.models_completed import CompletedTask
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core import management
from django.template import loader
from post_office import mail

from api.models import Operator, Registration

LOGGER = logging.getLogger(__name__)


@background(queue="outgoing-email")
def send_queued_mail():
    management.call_command("send_queued_mail")


@background(queue="membership-reminder")
def send_reminder_email():
    LOGGER.debug("Processing operator reminder emails...")

    expiry_date_begin = datetime.datetime.combine(
        datetime.datetime.now(pytz.utc), datetime.time(), tzinfo=pytz.utc
    ) + relativedelta(months=int(settings.REMINDER_EMAIL_NOTICE_MONTHS))
    expiry_date_end = datetime.datetime.combine(
        expiry_date_begin, datetime.time(23, 59, 59, 999999), tzinfo=pytz.utc
    )

    LOGGER.debug(
        "Processing registrations expiring between {} and {}".format(
            expiry_date_begin, expiry_date_end
        )
    )

    expiring_operators = Operator.objects.filter(
        registration_number__expiry_date__gt=expiry_date_begin,
        registration_number__expiry_date__lte=expiry_date_end,
    )

    email_list = []
    for operator in expiring_operators:
        reminder_email = {
            "sender": settings.AGRI_EMAIL,
            "recipients": [operator.email_address],
            "template": "reminder_email",
            "context": operator,
        }
        email_list.append(reminder_email)

    if len(email_list) > 0:
        LOGGER.info("Sending remider emails to {} operators".format(len(email_list)))
        mail.send_many(email_list)
    else:
        LOGGER.debug("No reminder emails to send this time.")


@background(queue="member-registration")
def send_registration_email(context: dict):
    """Send an email with the registration details to an operator. The data to be used to render the message
       and the certificate should be passed as a dictionary with the following structure:
       {
           "operator": operator, # an operator object,
           "registration_number": "DCR-12345" # a string representing the registration number
       }
    
    Arguments:
        context {dict} -- A dictionary to be used as context for rendering the email and the PDF certificate.
    """
    LOGGER.debug("send_registration_email(): context={}".format(context))

    template = loader.get_template("certificate/certificate.html")
    rendered = template.render(context)

    LOGGER.debug(
        "Requesting PDF certificate for {}".format(context["registration_number"])
    )
    response = requests.post(
        settings.WEASYPRINT_REQUEST_URL + "certificate.pdf",
        data=rendered,
        headers={"content-type": "text/html"},
    )

    TMP_DIR = tempfile.gettempdir()
    DEST_FILE = os.path.join(TMP_DIR, str(context["registration_number"]) + ".pdf")

    try:

        with open(DEST_FILE, "wb") as cert_file:
            cert_file.write(response.content)
            cert_file.close()

        LOGGER.debug(
            "Sending registration confirmation for registration #{}".format(
                context["registration_number"]
            )
        )
        mail.send(
            context["operator"]["email_address"],
            settings.AGRI_EMAIL,
            template="registration_email",  # Could be an EmailTemplate instance or name
            context=context,
            render_on_delivery=True,
            attachments={"{}.pdf".format(context["registration_number"]): DEST_FILE},
            # priority="now", # can't use now at this time: https://github.com/ui/django-post_office/issues/218
        )

    finally:
        # delete file when done
        if os.path.exists(DEST_FILE):
            LOGGER.debug("Removing temporary file {}".format(DEST_FILE))
            os.remove(DEST_FILE)

    LOGGER.info(
        "Registration confirmation sent to {}".format(
            context["operator"]["email_address"]
        )
    )


@background()
def update_registration_status():
    expired_registrations = Registration.objects.filter(
        expiry_date__lte=datetime.date.today(), operator_status=Registration.ACTIVE
    ).update(operator_status=Registration.CANCELLED)

    if expired_registrations > 0:
        LOGGER.info(
            "{} ACTIVE registration(s) have been marked as CANCELLED.".format(
                expired_registrations
            )
        )


@background()
def clear_old_tasks():
    # delete old completed tasks to prevent the background task table to become excessively big
    deleted_tasks = CompletedTask.objects.filter(
        run_at__lte=datetime.datetime.now()
    ).delete()
    LOGGER.debug(f"Deleted {deleted_tasks} old CompltedTask objects")
