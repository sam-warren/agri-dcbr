import json

from background_task import background
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

    mail.send(
        email_addr,
        template="registration_email",  # Could be an EmailTemplate instance or name
        context={"user": json.dumps(user), "registration_number": registration_number},
        render_on_delivery=True,
    )

    print("Registration confirmation sent to {}".format(email_addr))
