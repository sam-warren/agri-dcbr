from datetime import datetime

from dateutil.relativedelta import relativedelta
from django.conf import settings
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from email_service import tasks

from .models import Operator, Registration
from .serializers import Operator_Search_Serializer, Registration_Serializer


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

        animal_type = ""
        myOrderedDict = serializer.data["animal_risk_factors"]
        for record in myOrderedDict:
            myDict = dict(record)
            if animal_type == "":
                animal_type += myDict.pop("animal_type")
            else:
                animal_type = animal_type + " & " + myDict.pop("animal_type")

        # Send registration email
        registration_email_context = {
            "operator": serializer.data["operator"],
            "registration_number": serializer.data["registration_number"],
            "registration_date": registration_date.strftime("%B %d, %Y"),
            "expiry_date": expiry_date.strftime("%B %d, %Y"),
            "num_locations": len(serializer.data["addresses"]),
            "animal_type": animal_type,
        }
        tasks.send_registration_email(registration_email_context)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class Operator_Search_ViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    # add_model_type = False

    queryset = Operator.objects.none()
    serializer_class = Operator_Search_Serializer

    def filter_queryset(self, queryset):
        search_string = self.request.query_params.get("string", None)
        if search_string is not None:
            queryset = (
                Operator.objects.filter(
                    last_name__iexact=self.request.query_params["string"]
                )
                .union(
                    Operator.objects.filter(
                        registration_number__registration_number__iexact=self.request.query_params[
                            "string"
                        ]
                    )
                )
                .intersection(
                    Operator.objects.filter(
                        registration_number__operator_status=Registration.ACTIVE
                    )
                )
                .order_by("registration_number")
            )
        else:
            queryset = Operator.objects.none()

        return queryset

    _swagger_params = [
        openapi.Parameter(
            "string", openapi.IN_QUERY, description="Query string", type=openapi.TYPE_STRING
        )
    ]

    @swagger_auto_schema(manual_parameters=_swagger_params)
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
