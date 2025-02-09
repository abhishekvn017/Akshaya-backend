from django.db import models
from django.contrib.auth.models import AbstractUser
from myapp.models import Unit, PowerPlant



class CustomUser(AbstractUser):
    ROLES = (
        ('super_admin', 'Super Admin'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),

    )
    role = models.CharField(max_length=15, choices=ROLES,blank=True, null=True)
    staff_name = models.CharField(max_length=255, null=False)
    power_plant = models.ForeignKey(PowerPlant, on_delete=models.CASCADE, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True)
    staff_mob = models.CharField(max_length=255, null=False)


    def isAdmin(self):
        return self.is_superuser or self.role == 'admin'