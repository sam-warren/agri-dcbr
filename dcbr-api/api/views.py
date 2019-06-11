from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from api.serializers import (
    Operator_Serializer,
    Address_Serializer,
    Risk_Factor_Animal_Serializer,
    Risk_Factor_Operation_Serializer,
    Inspection_Serializer,
    Association_Membership_Serializer,
)

# from api.models import Category, Entry, Operator, Address
from api.models import (
    Operator,
    Address,
    Inspection,
    Risk_Factor_Animal,
    Risk_Factor_Operation,
    Association_Membership,
)


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


class Risk_Factor_Animal_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Inspection.objects.all()
    serializer_class = Risk_Factor_Animal_Serializer


class Risk_Factor_Operation_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Inspection.objects.all()
    serializer_class = Risk_Factor_Operation_Serializer


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

