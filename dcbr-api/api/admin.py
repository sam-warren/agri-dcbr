from django.contrib import admin
from api.models import (
    Operator,
    Address,
    Inspection,
    Risk_Factor_MetaData,
    Risk_Factor_Data,
    Association_Membership,
)

admin.site.register(Operator)
admin.site.register(Address)
admin.site.register(Inspection)
admin.site.register(Risk_Factor_MetaData)
admin.site.register(Risk_Factor_Data)
admin.site.register(Association_Membership)
