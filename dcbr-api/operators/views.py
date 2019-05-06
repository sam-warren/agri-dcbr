from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import OperatorSerializer      # add this
from .models import Operator                     # add this

class OperatorView(viewsets.ModelViewSet):       # add this
    serializer_class = OperatorSerializer          # add this
    queryset = Operator.objects.all()              # add this