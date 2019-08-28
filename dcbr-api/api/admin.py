from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

# from import_export.admin import ExportActionAdmin
from api.resources import AddressResource

from import_export.formats import base_formats


class MyAdmin(ExportMixin):
    # your normal stuff
    def get_export_formats(self):
        """
            Returns available export formats.
            """
        formats = (base_formats.CSV,)
        return [f for f in formats if f().can_export()]


from api.models import (
    Registration_Number,
    Operator,
    Address,
    Inspection,
    Operation_Risk_Factor,
    Animal_Risk_Factor,
    Association_Membership,
)


class Registration_NumberAdmin(MyAdmin, admin.ModelAdmin):
    pass


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


admin.site.register(Registration_Number, Registration_NumberAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Inspection, InspectionAdmin)
admin.site.register(Operation_Risk_Factor, Operation_Risk_FactorAdmin)
admin.site.register(Animal_Risk_Factor, Animal_Risk_FactorAdmin)
admin.site.register(Association_Membership, Association_MembershipAdmin)

