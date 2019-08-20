from rest_framework.serializers import ModelSerializer

from api.models import (
    RegistrationNumber,
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
            "address_type",
            "street_num",
            "suite",
            "street_name",
            "city",
            "postal_code",
        )


class Association_Membership_Serializer(ModelSerializer):
    class Meta:
        model = Association_Membership
        fields = ("id", "assoc_name", "membership_num", "assoc_URL")


class Risk_Factor_Operation_Serializer(ModelSerializer):
    class Meta:
        model = Risk_Factor_Operation
        fields = (
            "id",
            "accidental_breeding",
            "num_workers",
            "animal_type",
            "num_breeds_dogs",
            "num_breeds_cats",
            "has_vet",
            "has_perm_id",
            "perm_id_type",
            "perm_id_other",
        )


class Risk_Factor_Animal_Serializer(ModelSerializer):
    class Meta:
        model = Risk_Factor_Animal
        fields = (
            "id",
            "num_dogs_intact",
            "num_litter_whelped",
            "num_cats_intact",
            "num_litter_queened",
            "num_dog_sold",
            "num_dog_transferred",
            "num_dog_traded",
            "num_dog_leased",
            "num_cat_sold",
            "num_cat_transferred",
            "num_cat_traded",
            "num_cat_leased",
        )


class Operator_Serializer(ModelSerializer):
    class Meta:
        model = Operator
        fields = (
            "id",
            "first_name",
            "middle_name",
            "last_name",
            "comm_pref",
            "phone_num",
            "email_address",
            "operation_type",
            "operation_name",
            "operation_URL",
            "comm_pref",
        )

class RegistrationNumber_Serializer(ModelSerializer):
    operator = Operator_Serializer()
    addresses = Address_Serializer(many=True)
    associations = Association_Membership_Serializer(many=True)
    risk_factor_animals = Risk_Factor_Animal_Serializer(many=True)
    risk_factor_operations = Risk_Factor_Operation_Serializer(many=True)

    class Meta:
        model = RegistrationNumber
        fields = (
            "id",
            "operator_status",
            "operator",
            "addresses",
            "associations",
            "risk_factor_animals",
            "risk_factor_operations",
        )

    def create(self, validated_data):
        print(validated_data)

        operator_data = validated_data.pop("operator")
        risk_factor_animals_data = validated_data.pop("risk_factor_animals")
        associations_data = validated_data.pop("associations")
        addresses_data = validated_data.pop("addresses")
        risk_factor_operations_data = validated_data.pop("risk_factor_operations")

        registrationNumber = RegistrationNumber.objects.create(**validated_data)

        for address_data in addresses_data:
            Address.objects.create(
                registrationNumber=registrationNumber, **address_data
            )
        for association_data in associations_data:
            Association_Membership.objects.create(
                registrationNumber=registrationNumber, **association_data
            )
        for risk_factor_animal_data in risk_factor_animals_data:
            Risk_Factor_Animal.objects.create(
                registrationNumber=registrationNumber, **risk_factor_animal_data
            )

        for risk_factor_operation_data in risk_factor_operations_data:
            Risk_Factor_Operation.objects.create(
                registrationNumber=registrationNumber, **risk_factor_operation_data
            )
       
        Operator.objects.create(registrationNumber=registrationNumber, **operator_data)

        return registrationNumber


class Inspection_Serializer(ModelSerializer):
    class Meta:
        model = Inspection
        fields = "__all__"

