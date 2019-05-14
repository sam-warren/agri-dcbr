from rest_framework import serializers
from .models import Operator

class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('id', 'name', 'address1', 'numDogs', 'numCats', 'timestamp', 'completed')