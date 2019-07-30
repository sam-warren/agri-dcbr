import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .tasks import send_registration_email

LOGGER = logging.getLogger(__name__)


class EmailNotification(APIView):
    def post(self, request, user_id):

        # user_id = self.kwargs["user_id"]

        try:
            send_registration_email(user_id)
            return Response(status=status.HTTP_200_OK)

        except Exception:
            LOGGER.error(
                "Email notification for user with id {} was not sent correctly".format(
                    user_id
                )
            )
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
