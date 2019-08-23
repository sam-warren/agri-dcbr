import logging
import os
import tempfile

import requests
from background_task import background
from django.conf import settings
from django.core import management
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

    user = {"name": "DCBR Operator " + email_addr, "other_prop": "other_value"}

    registration_number = "DCBR-123456"

    LOGGER.debug(
        "Requesting PDF certificate for registration #{}".format(registration_number)
    )
    response = requests.post(
        settings.WEASYPRINT_REQUEST_URL + "certificate.pdf",
        data="<h1>TEST CERTIFICATE</h1><p>A paragraph.</p>",
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
                "user": user,
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
