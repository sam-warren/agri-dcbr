from background_task import background


@background(queue="membership-reminder")
def send_reminder_email():
    # TODO: implement logic
    print("Sending new reminder emails to operators...")


@background(queue="member-registration")
def send_registration_email(user_id):
    # TODO: implement logic, see https://github.com/ui/django-post_office#usage
    print("Sending registration email for user {}".format(user_id))
