from background_task import background


@background(queue="membership-reminder")
def send_reminder_email():
    # TODO: implement logic
    print("Sending new reminder emails to operators...")
