from django.contrib import admin
from myapp.models import PowerPlant,Unit,Maintenance,Inspection,Resource

# Register your models here.
admin.site.register([PowerPlant, Unit, Maintenance, Inspection, Resource])
