from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.conf import settings
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from email_service import tasks

from .models import Registration
from .serializers import Registration_Serializer


class Registration_ViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    A simple ViewSet for viewing and editing registration numbers.
    """

    queryset = Registration.objects.all()
    serializer_class = Registration_Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Calculate expiry date
        registration_date = datetime.strptime(
            serializer.data["registration_date"][0:10], "%Y-%m-%d"
        )
        expiry_date = registration_date + relativedelta(
            months=int(settings.REGISTRATION_VALIDITY_MONTHS)
        )

        # Send registration email
        registration_email_context = {
            "operator": serializer.data["operator"],
            "registration_number": serializer.data["registration_number"],
            "registration_date": registration_date.strftime("%B %d, %Y"),
            "expiry_date": expiry_date.strftime("%B %d, %Y"),
            "num_locations": serializer.data["num_locations"],
        }
        tasks.send_registration_email(registration_email_context)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
