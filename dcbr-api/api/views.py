from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from api.serializers import (
    Registration_Serializer,
    Operator_Serializer,
    Address_Serializer,
    Animal_Risk_Factor_Serializer,
    Operation_Risk_Factor_Serializer,
    Inspection_Report_Serializer,
    Renewal_Serializer,
    Association_Membership_Serializer,
)

# from api.models import Category, Entry, Operator, Address
from api.models import (
    Registration,
    Operator,
    Address,
    Inspection_Report,
    Animal_Risk_Factor,
    Operation_Risk_Factor,
    Renewal,
    Association_Membership,
)


class Registration_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing registration numbers.
    """

    queryset = Registration.objects.all()
    serializer_class = Registration_Serializer

    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
