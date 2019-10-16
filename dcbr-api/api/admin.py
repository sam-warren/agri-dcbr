from django.conf.urls import url
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

# from import_export.admin import ExportActionAdmin
from api.resources import AddressResource

from import_export.formats import base_formats

from api.models import (
    Registration,
    Operator,
    Address,
    Inspection_Report,
    Operation_Risk_Factor,
    Animal_Risk_Factor,
    Renewal,
    Association_Membership,
)


class MyAdmin(ExportMixin):
    # your normal stuff
    def get_export_formats(self):
        """
            Returns available export formats.
            """
        formats = (base_formats.CSV,)
        return [f for f in formats if f().can_export()]


class OperatorInline(admin.StackedInline):
    model = Operator


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0


class AssociationsInline(admin.StackedInline):
    model = Association_Membership
    extra = 0


class Operation_Risk_FactorInline(admin.StackedInline):
    model = Operation_Risk_Factor
    extra = 0


class Animal_Risk_FactorInline(admin.StackedInline):
    model = Animal_Risk_Factor
    extra = 0


class RenewalInline(admin.StackedInline):
    model = Renewal
    extra = 0


class OperatorAdmin(MyAdmin, admin.ModelAdmin):
    pass
    list_display = ("registration_number", "first_name", "last_name","operation_type")
    list_filter = ("registration_number", "first_name", "last_name","operation_type")
    search_fields = ("registration_number__registration_number", "first_name", "last_name","operation_type")


class AddressAdmin(MyAdmin, admin.ModelAdmin):
    pass
    list_display = ("registration_number", "street_num", "street_name","POBox", "city", "region")
    list_filter = ("registration_number", "city", "region")
    search_fields = ("registration_number__registration_number", "street_num", "street_name","POBox", "city", "region")


class Inspection_ReportAdmin(MyAdmin, admin.ModelAdmin):
    pass
    list_display = ("registration_number", "inspector_full_name", "operator_first_name", "operator_last_name","created_date", "updated_date")
    list_filter = ("registration_number", "inspector_full_name", "operator_first_name", "operator_last_name","created_date", "updated_date")
    search_fields = ("registration_number__registration_number", "inspector_full_name", "operator_first_name", "operator_last_name","created_date", "updated_date")


class Operation_Risk_FactorAdmin(MyAdmin, admin.ModelAdmin):
    pass
    list_display = ("registration_number", "accidental_breeding", "num_workers", "has_vet", "has_perm_id")
    list_filter = ("registration_number", "accidental_breeding", "num_workers", "has_vet", "has_perm_id")
    search_fields = ("registration_number__registration_number", "accidental_breeding", "num_workers", "has_vet", "has_perm_id")


class Animal_Risk_FactorAdmin(MyAdmin, admin.ModelAdmin):
    pass
    list_display = ("registration_number", "animal_type", "num_breeds", "num_females_intact", "num_litter", "num_sold", "num_animals")
    list_filter = ("registration_number", "animal_type")
    search_fields = ("registration_number__registration_number", "animal_type", "num_breeds", "num_females_intact", "num_litter", "num_sold", "num_animals")


class Association_MembershipAdmin(MyAdmin, admin.ModelAdmin):
    pass
    list_display = ("registration_number", "assoc_name")
    list_filter = ("registration_number", "assoc_name")
    search_fields = ("registration_number__registration_number", "assoc_name")

class RenewalAdmin(MyAdmin, admin.ModelAdmin):
    pass
    list_display = ("registration_number", "first_name","last_name", "previous_registration_number", "previous_registration_date")
    list_filter = ("registration_number", "first_name","last_name", "previous_registration_number")
    search_fields = ("registration_number__registration_number", "first_name","last_name", "previous_registration_number", "previous_registration_date")


class RegistrationAdmin(MyAdmin, admin.ModelAdmin):
    pass
    list_display = ("registration_number", "operator_status", "registration_date")
    list_filter = ("operator_status", "updated_date")
    search_fields = ("registration_number", "registration_date")
    inlines = (
        OperatorInline,
        AddressInline,
        AssociationsInline,
        Operation_Risk_FactorInline,
        Animal_Risk_FactorInline,
        RenewalInline,
    )


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Inspection_Report, Inspection_ReportAdmin)
admin.site.register(Operation_Risk_Factor, Operation_Risk_FactorAdmin)
admin.site.register(Animal_Risk_Factor, Animal_Risk_FactorAdmin)
admin.site.register(Association_Membership, Association_MembershipAdmin)
admin.site.register(Renewal, RenewalAdmin)

