from rest_framework import serializers
from .models import PowerPlant, Unit, Maintenance, Inspection, Resource,Household, SmallCommercial

class PowerPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerPlant
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'

class InspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'

# class StaffSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Staff
#         fields = '__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class HouseholdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Household
        fields = '__all__'

class SmallCommercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmallCommercial
        fields = '__all__'
