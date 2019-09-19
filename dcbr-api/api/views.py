from rest_framework.response import Response
from rest_framework import viewsets
from email_service import tasks
from rest_framework import mixins, status

from api.serializers import Registration_Serializer

# from api.models import Category, Entry, Operator, Address
from api.models import Registration


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

        # Send registration email
        registration_email_context = {
            "operator": serializer.data["operator"],
            "registration_number": serializer.data["registration_number"],
            "registration_date": serializer.data["registration_date"],
            "expiry_date": serializer.data["expiry_date"],
        }
        tasks.send_registration_email(registration_email_context)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
