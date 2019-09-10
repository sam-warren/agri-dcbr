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
    Inspection,
    Operation_Risk_Factor,
    Animal_Risk_Factor,
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


class OperatorAdmin(MyAdmin, admin.ModelAdmin):
    pass


class AddressAdmin(MyAdmin, admin.ModelAdmin):
    pass


class InspectionAdmin(MyAdmin, admin.ModelAdmin):
    pass


class Operation_Risk_FactorAdmin(MyAdmin, admin.ModelAdmin):
    pass


class Animal_Risk_FactorAdmin(MyAdmin, admin.ModelAdmin):
    pass


class Association_MembershipAdmin(MyAdmin, admin.ModelAdmin):
    pass


class RegistrationAdmin(MyAdmin, admin.ModelAdmin):
    pass
    inlines = (
        OperatorInline,
        AddressInline,
        AssociationsInline,
        Operation_Risk_FactorInline,
        Animal_Risk_FactorInline,
    )


admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Operation_Risk_Factor, Operation_Risk_FactorAdmin)
admin.site.register(Animal_Risk_Factor, Animal_Risk_FactorAdmin)
admin.site.register(Association_Membership, Association_MembershipAdmin)

