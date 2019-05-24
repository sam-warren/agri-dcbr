from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from api.serializers import CategorySerializer, EntrySerializer
from api.models import Category, Entry


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EntryViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing entries.
    """
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
