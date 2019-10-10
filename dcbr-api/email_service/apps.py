from django.apps import AppConfig
from django.db.models.signals import post_migrate
import logging

LOGGER = logging.getLogger(__name__)


def start_reminder_email_task(sender, **kwargs):
    from .tasks import send_reminder_email, send_queued_mail, update_registration_status

    # reminder emails are scheduled to run daily
    send_reminder_email(repeat=60 * 60 * 24, repeat_until=None)

    # queued mail is processed every minute
    send_queued_mail(repeat=60 * 60 * 24, repeat_until=None)

    update_registration_status(repeat=60, repeat_until=None)


class EmailServiceConfig(AppConfig):
    name = "email_service"
    verbose_name = "DCBR Email Service"

    def ready(self):
        # start email reminder task once migrations have completed
        post_migrate.connect(start_reminder_email_task, sender=self)
