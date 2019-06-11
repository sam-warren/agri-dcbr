from rest_framework.serializers import ModelSerializer

# from api.models import Category, Entry, Operator, Address
from api.models import (
    Operator,
    Address,
    Inspection,
    Risk_Factor_Operation,
    Risk_Factor_Animal,
    Association_Membership,
    Inspection,
)


class Address_Serializer(ModelSerializer):
    class Meta:
        model = Address
        fields = (
            "id",
            "type",
            "street_num",
            "suite",
            "street_name",
            "city",
            "postal_code",
        )


class Association_Membership_Serializer(ModelSerializer):
    class Meta:
        model = Association_Membership
        # unique_together('operator', 'regNum')
        # fields = "__all__"
        fields = ("id", "assoc_name", "membership_num", "assoc_URL")


class Risk_Factor_Operation_Serializer(ModelSerializer):
    class Meta:
        model = Risk_Factor_Operation
        # unique_together('operator', 'regNum')
        # fields = "__all__"

        fields = (
            "id",
            "accidental_breeding",
            "num_workers",
            "operation_URL",
            "num_breeds_dogs",
            "num_breeds_cats",
            "has_vet",
            "has_perm_id",
            "perm_id_type",
            "perm_id_other",
        )
        # read_only_fields = ("regNum",)


class Risk_Factor_Animal_Serializer(ModelSerializer):
    class Meta:
        model = Risk_Factor_Animal
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


class Operator_Serializer(ModelSerializer):
    addresses = Address_Serializer(many=True)
    associations = Association_Membership_Serializer(many=True)
    risk_factor_animals = Risk_Factor_Animal_Serializer(many=True)
    # risk_factor_operations = Risk_Factor_Operation_Serializer(many=True)

    class Meta:
        model = Operator
        # fields = "__all__"
        fields = (
            "id",
            "reg_num",
            "first_name",
            "middle_name",
            "last_name",
            "addresses",
            "associations",
            "risk_factor_animals",
            # "risk_factor_operations",
        )
        read_only_fields = ("reg_num",)

    def create(self, validated_data):
        print("inside create")
        print(validated_data)

        risk_factor_animals_data = validated_data.pop("risk_factor_animals")
        associations_data = validated_data.pop("associations")
        addresses_data = validated_data.pop("addresses")
        # risk_factor_operations_data = validated_data.pop("risk_factor_operations")

        operator = Operator.objects.create(**validated_data)

        for address_data in addresses_data:
            Address.objects.create(operator=operator, **address_data)
        for association_data in associations_data:
            Association_Membership.objects.create(operator=operator, **association_data)
        for risk_factor_animal_data in risk_factor_animals_data:
            Risk_Factor_Animal.objects.create(
                operator=operator, **risk_factor_animal_data
            )
        # for risk_factor_operation_data in risk_factor_operations_data:
        #     Risk_Factor_Operation.objects.create(
        #         operator=operator, **risk_factor_operation_data
        #     )

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
        instance.first_name = validated_data.get("firstName", instance.first_name)
        instance.middle_name = validated_data.get("middleName", instance.middle_name)
        instance.last_name = validated_data.get("lastName", instance.last_name)
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


class Inspection_Serializer(ModelSerializer):
    class Meta:
        model = Inspection
        fields = "__all__"

