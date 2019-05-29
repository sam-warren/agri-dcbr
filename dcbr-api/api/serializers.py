from rest_framework.serializers import ModelSerializer

# from api.models import Category, Entry, Operator, Address
from api.models import Operator, Address


# class CategorySerializer(ModelSerializer):
#    class Meta:
#        model = Category
#        fields = "__all__"


# class EntrySerializer(ModelSerializer):
#    class Meta:
#        model = Entry
#        fields = "__all__"


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        # unique_together('operator', 'regNum')
        # fields = "__all__"
        fields = ("type", "streetNum", "suite", "streetName", "city", "postalCode")
        # read_only_fields = ("regNum",)


class OperatorSerializer(ModelSerializer):
    addresses = AddressSerializer(many=True)

    class Meta:
        model = Operator
        fields = "__all__"
        # fields = ('regNum', 'firstName', 'middleName', 'lastName', 'address')
        read_only_fields = ("regNum",)

    def create(self, validated_data):
        addresses_data = validated_data.pop("addresses")
        operator = Operator.objects.create(**validated_data)
        for address_data in addresses_data:
            Address.objects.create(operator=operator, **address_data)
        return operator

