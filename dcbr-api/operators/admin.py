from django.contrib import admin
from .models import Operator # add this

class OperatorAdmin(admin.ModelAdmin):  # add this
    list_display = ('name', 'address1', 'numDogs', 'numCats', 'completed') # add this

# Register your models here.
admin.site.register(Operator, OperatorAdmin) # add this