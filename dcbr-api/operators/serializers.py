from rest_framework import serializers
from .models import Operator

class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('regNum', 'firstName', 'middleName', 'lastName', 'streetName', 'aptNum', 'streetName', 'city', 'postalCode', 'province', 'phoneNum', 'email')