from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# Create a single instance of DefaultRouter
router = DefaultRouter()

# Register your viewsets with the router
router.register(r'powerplants', views.PowerPlantViewSet)
router.register(r'units', views.UnitViewSet)
router.register(r'maintenance', views.MaintenanceViewSet)
router.register(r'inspections', views.InspectionViewSet)
# router.register(r'staff', views.StaffViewSet)
router.register(r'resources', views.ResourceViewSet)

# Register additional viewsets if needed
router.register(r'households', views.HouseholdViewSet)
router.register(r'small-commercials', views.SmallCommercialViewSet)

# Define the urlpatterns list
urlpatterns = [
    path('', include(router.urls)),
    
]