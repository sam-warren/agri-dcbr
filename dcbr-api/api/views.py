from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from api.serializers import (
    # CategorySerializer,
    # EntrySerializer,
    OperatorSerializer,
    AddressSerializer,
    Risk_Factor_Animals_Serializer,
    Risk_Factor_Operation_Serializer,
    InspectionSerializer,
    Association_Membership_Serializer,
)

# from api.models import Category, Entry, Operator, Address
from api.models import (
    Operator,
    Address,
    Inspection,
    Risk_Factor_Animals,
    Risk_Factor_Operation,
    Association_Membership,
)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing categories.
    """

    # queryset = Category.objects.all()
    # serializer_class = CategorySerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing entries.
    """

    # queryset = Entry.objects.all()
    # serializer_class = EntrySerializer


class OperatorViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing operators.
    """

    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer


class AddressViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class Risk_Factor_Animals_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Inspection.objects.all()
    serializer_class = Risk_Factor_Animals_Serializer


class Risk_Factor_Operation_ViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Inspection.objects.all()
    serializer_class = Risk_Factor_Operation_Serializer


class InspectionViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer


class AssociationViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing addresses.
    """

    queryset = Inspection.objects.all()
    serializer_class = Association_Membership_Serializer

