import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import send_registration_email

LOGGER = logging.getLogger(__name__)


class EmailNotification(APIView):
    def put(self, request, *args, **kwargs):

        email_addr = self.kwargs["email_addr"]

        try:
            send_registration_email(email_addr)
            return Response(status=status.HTTP_200_OK)

        except Exception:
            LOGGER.error(
                "Email notification for user with id {} was not sent correctly".format(
                    email_addr
                )
            )
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
