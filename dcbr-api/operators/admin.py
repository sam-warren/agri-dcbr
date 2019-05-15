from django.contrib import admin
from .models import Operator # add this

class OperatorAdmin(admin.ModelAdmin):  # add this
    list_display = ('regNum', 'firstName', 'middleName', 'lastName', 'streetName', 'aptNum', 'streetName', 'city', 'postalCode', 'province', 'phoneNum', 'email', 'completed', 'timestamp')

# Register your models here.
admin.site.register(Operator, OperatorAdmin) # add this