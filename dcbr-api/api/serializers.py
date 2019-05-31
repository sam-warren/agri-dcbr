from rest_framework.serializers import ModelSerializer

# from api.models import Category, Entry, Operator, Address
from api.models import (
    Operator,
    Address,
    Inspection,
    Risk_Factor_MetaData,
    Risk_Factor_Data,
    Association_Membership,
    Inspection,
)


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
        fields = (
            "id",
            "type",
            "streetNum",
            "suite",
            "streetName",
            "city",
            "postalCode",
        )
        # read_only_fields = ("regNum",)


class OperatorSerializer(ModelSerializer):
    addresses = AddressSerializer(many=True)

    class Meta:
        model = Operator
        fields = "__all__"
        # fields = ('id', 'regNum', 'firstName', 'middleName', 'lastName', 'address')
        read_only_fields = ("regNum",)

    def create(self, validated_data):
        addresses_data = validated_data.pop("addresses")
        operator = Operator.objects.create(**validated_data)
        for address_data in addresses_data:
            Address.objects.create(operator=operator, **address_data)
        return operator

    # def update(self, instance, validated_data):
    #     addresses_data = validated_data.pop("addresses")
    #     instance.firstName = validated_data.get("firstName", instance.firstName)
    #     instance.middleName = validated_data.get("middleName", instance.middleName)
    #     instance.lastName = validated_data.get("lastName", instance.lastName)
    #     instance.save()

    #     # address = Address.objects.create(**validated_data)
    #     for address_data in addresses_data:
    #         print(address_data)
    #         # address = Address.objects.get(pk=address_data.id)
    #         # address.save(**address_data)
    #     return instance

    def update(self, instance, validated_data):
        addresses_data = validated_data.pop("addresses")
        instance.firstName = validated_data.get("firstName", instance.firstName)
        instance.middleName = validated_data.get("middleName", instance.middleName)
        instance.lastName = validated_data.get("lastName", instance.lastName)
        instance.save()

        for address_data in addresses_data:
            address_id = address_data.get("id", None)

        if address_id:
            address = Address.objects.get(id=address_id, operator=instance)
            # Set all attributes here. Adding only streetName for now.
            address.streetName = address_data.get("streetName")
            address.save()
        else:  # This is to handle any new addition of address during operator PUT
            address = Address.objects.create(operator=instance, **address_data)
        return instance


class Risk_Factor_MetaData_Serializer(ModelSerializer):
    class Meta:
        model = Risk_Factor_MetaData
        # unique_together('operator', 'regNum')
        # fields = "__all__"
        fields = (
            "id",
            "accidental_breeding",
            "num_workers",
            "opn_URL",
            "num_breeds_dogs",
            "num_breeds_cats",
            "has_vet",
            "has_perm_id",
            "perm_id_type",
            "perm_id_other",
        )
        # read_only_fields = ("regNum",)


class Risk_Factor_Data_Serializer(ModelSerializer):
    class Meta:
        model = Risk_Factor_Data
        # unique_together('operator', 'regNum')
        # fields = "__all__"
        fields = (
            "id",
            "num_dogs_intact",
            "num_litter_whelped",
            "num_cats_intact",
            "num_litter_queened",
            "num_sold",
            "num_transferred",
            "num_traded",
            "num_leased",
        )

        # read_only_fields = ("regNum",)


class Association_Membership_Serializer(ModelSerializer):
    class Meta:
        model = Association_Membership
        # unique_together('operator', 'regNum')
        # fields = "__all__"
        fields = ("id", "assoc_name", "membership_num", "assoc_URL")


class InspectionSerializer(ModelSerializer):
    class Meta:
        model = Inspection
        fields = "__all__"

