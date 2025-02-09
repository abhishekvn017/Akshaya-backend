from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from users.permissions import IsAdmin
from .models import PowerPlant, Unit, Maintenance, Inspection, Resource, Household, SmallCommercial
from .serializers import PowerPlantSerializer, UnitSerializer, MaintenanceSerializer, InspectionSerializer, ResourceSerializer,HouseholdSerializer, SmallCommercialSerializer

class PowerPlantViewSet(viewsets.ModelViewSet):
    queryset = PowerPlant.objects.all()
    serializer_class = PowerPlantSerializer
    permission_classes = [AllowAny]


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [AllowAny]

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

class InspectionViewSet(viewsets.ModelViewSet):
    queryset = Inspection.objects.all()
    serializer_class = InspectionSerializer

# class StaffViewSet(viewsets.ModelViewSet):
#     queryset = Staff.objects.all()
#     serializer_class = StaffSerializer

class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    
class HouseholdViewSet(viewsets.ModelViewSet):
    queryset = Household.objects.all()
    serializer_class = HouseholdSerializer

class SmallCommercialViewSet(viewsets.ModelViewSet):
    queryset = SmallCommercial.objects.all()
    serializer_class = SmallCommercialSerializer

