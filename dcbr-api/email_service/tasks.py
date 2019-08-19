import json

import django.conf
import requests
from background_task import background
from django.conf import settings
from django.core.files.base import ContentFile
from post_office import mail


@background(queue="membership-reminder")
def send_reminder_email():
    # TODO: implement logic
    print("Sending new reminder emails to operators...")


@background(queue="member-registration")
def send_registration_email(email_addr):
    # TODO: update email logic, refer to https://github.com/ui/django-post_office#usage

    user = {"name": "DCBR Operator " + email_addr, "other_prop": "other_value"}

    registration_number = "DCBR-123456"

    response = requests.post(
        settings.WEASYPRINT_REQUEST_URL + "certificate.pdf",
        data="<h1>TEST CERTIFICATE</h1><p>A paragraph.</p>",
        headers={"content-type": "text/html"},
    )

    mail.send(
        ["AgriServiceBC@gov.bc.ca"],
        email_addr,
        template="registration_email",  # Could be an EmailTemplate instance or name
        context={"user": json.dumps(user), "registration_number": registration_number},
        render_on_delivery=True,
        attachments={"certificate.pdf": ContentFile(response.content)},
    )

    print("Registration confirmation sent to {}".format(email_addr))
