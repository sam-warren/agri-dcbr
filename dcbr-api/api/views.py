from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from api.serializers import (
    Registration_Serializer,
    Operator_Serializer,
    Address_Serializer,
    Animal_Risk_Factor_Serializer,
    Operation_Risk_Factor_Serializer,
    Inspection_Serializer,
    Association_Membership_Serializer,
)

# from api.models import Category, Entry, Operator, Address
from api.models import (
    Registration,
    Operator,
    Address,
    Inspection,
    Animal_Risk_Factor,
    Operation_Risk_Factor,
    Association_Membership,
)


class Registration_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing registration numbers.
    """

    queryset = Registration.objects.all()
    serializer_class = Registration_Serializer


class Operator_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing operators.
    """

    queryset = Operator.objects.all()
    serializer_class = Operator_Serializer


class Address_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Address.objects.all()
    serializer_class = Address_Serializer


class Animal_Risk_Factor_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Inspection.objects.all()
    serializer_class = Animal_Risk_Factor_Serializer


class Operation_Risk_Factor_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Inspection.objects.all()
    serializer_class = Operation_Risk_Factor_Serializer


class Inspection_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Inspection.objects.all()
    serializer_class = Inspection_Serializer


class Association_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Inspection.objects.all()
    serializer_class = Association_Membership_Serializer

