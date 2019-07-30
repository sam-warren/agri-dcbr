from django.apps import AppConfig
from django.db.models.signals import post_migrate


def start_reminder_email_task(sender, **kwargs):
    from .tasks import send_reminder_email

    send_reminder_email(repeat=15, repeat_until=None)


class EmailServiceConfig(AppConfig):
    name = "email_service"
    verbose_name = "DCBR Email Service"

    def ready(self):
        # start email reminder task once migrations have completed
        post_migrate.connect(start_reminder_email_task, sender=self)
