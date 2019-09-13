import datetime
import json
import logging
import os
import tempfile

import requests
from background_task import background
from dateutil.relativedelta import relativedelta
from django.conf import settings
from django.core import management
from django.template import loader
from post_office import mail

LOGGER = logging.getLogger(__name__)


@background(queue="outgoing-email")
def send_queued_mail():
    management.call_command("send_queued_mail")


@background(queue="membership-reminder")
def send_reminder_email():
    # TODO: implement logic
    LOGGER.debug("Sending new reminder emails to operators...")


@background(queue="member-registration")
def send_registration_email(email_addr):
    # TODO: update email logic, refer to https://github.com/ui/django-post_office#usage

    operator = {"name": email_addr, "other_prop": "other_value"}
    registration_number = "DCBR-123456"
    locations_num = 2
    animal_types = "Dogs"
    operation_type = "Seller"
    expiry_date = datetime.datetime.now() + relativedelta(minutes=1)

    template_context = {
        "operator": operator,
        "registration_number": registration_number,
        "locations_num": locations_num,
        "animal_types": animal_types,
        "operation_type": operation_type,
        "renewal_date": renewal_date.strftime("%B %d, %Y"),
    }

    template = loader.get_template("certificate/certificate.html")
    rendered = template.render(template_context)

    LOGGER.debug(
        "Requesting PDF certificate for registration #{}".format(registration_number)
    )
    response = requests.post(
        settings.WEASYPRINT_REQUEST_URL + "certificate.pdf",
        data=rendered,
        headers={"content-type": "text/html"},
    )

    TMP_DIR = tempfile.gettempdir()
    DEST_FILE = os.path.join(TMP_DIR, registration_number + ".pdf")

    try:

        with open(DEST_FILE, "wb") as cert_file:
            cert_file.write(response.content)
            cert_file.close()

        LOGGER.debug(
            "Sending registration confirmation for registration #{}".format(
                registration_number
            )
        )
        mail.send(
            email_addr,
            settings.AGRI_EMAIL,
            template="registration_email",  # Could be an EmailTemplate instance or name
            context={
                "user": json.dumps(operator),
                "registration_number": registration_number,
            },
            render_on_delivery=True,
            attachments={"certificate.pdf": DEST_FILE},
            # priority="now", # can't use now at this time: https://github.com/ui/django-post_office/issues/218
        )

    finally:
        # delete file when done
        if os.path.exists(DEST_FILE):
            LOGGER.debug("Removing temporary file {}".format(DEST_FILE))
            os.remove(DEST_FILE)

    LOGGER.info("Registration confirmation sent to {}".format(email_addr))
