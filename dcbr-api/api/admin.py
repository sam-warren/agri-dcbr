from django.contrib import admin
from api.models import (
    Registration_Number,
    Operator,
    Address,
    Inspection,
    Operation_Risk_Factor,
    Animal_Risk_Factor,
    Association_Membership,
)

admin.site.register(Registration_Number)
admin.site.register(Operator)
admin.site.register(Address)
admin.site.register(Inspection)
admin.site.register(Operation_Risk_Factor)
admin.site.register(Animal_Risk_Factor)
admin.site.register(Association_Membership)
