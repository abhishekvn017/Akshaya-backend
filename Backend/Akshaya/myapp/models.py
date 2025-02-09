from django.db import models

class PowerPlant(models.Model):
    plant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.DecimalField(max_digits=10, decimal_places=2)  # Capacity in MW
    TYPE_OF_ENERGY_CHOICES = [
        ('solar', 'Solar'),
        ('wind', 'Wind'),
        ('hydro', 'Hydro'),
        ('tidal', 'Tidal'),
    ]
    type_of_energy = models.CharField(max_length=10, choices=TYPE_OF_ENERGY_CHOICES)

    def __str__(self):
        return self.name


class Unit(models.Model):
    unit_id = models.AutoField(primary_key=True)
    power_plant = models.ForeignKey(PowerPlant, on_delete=models.CASCADE, null=True, blank=True)
    unit_name = models.CharField(max_length=100)
    # status = models.CharField(max_length=20)
    # last_maintenance_date = models.DateField()
    # next_inspection_date = models.DateField()

    def __str__(self):
        return self.unit_name


class Maintenance(models.Model):
    record_id = models.AutoField(primary_key=True)
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)
    maintenance_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    maintenance_type = models.CharField(max_length=100)
    performed_by = models.CharField(max_length=100, null=True)
    record_specifications = models.TextField()

    def __str__(self):
        return f"Record {self.record_id} for Unit {self.unit_id}"


class Inspection(models.Model):
    INSPECTION_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    inspection_id = models.AutoField(primary_key=True)
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)  # Adjust the max_length as needed
    inspection_date = models.DateField()
    inspection_status = models.CharField(max_length=20, choices=INSPECTION_STATUS_CHOICES, default='pending')
    comments = models.TextField(blank=True, null=True)
    inspected_by = models.CharField(max_length=100, null=True)  # Adjust the max_length as needed
    completed_by = models.CharField(max_length=100, blank=True, null=True)  # Adjust the max_length as needed

    def __str__(self):
        return f"Inspection {self.inspection_id} - {self.unit_id}"


# class Staff(models.Model):
#     staff_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     role = models.CharField(max_length=50)
#     contact_info = models.CharField(max_length=200)
#     designed_units = models.JSONField()

#     def __str__(self):
#         return self.name


class Resource(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Household(models.Model):
    name = models.CharField(max_length=255)
    solar_generation = models.FloatField(help_text="Solar energy generated in kWh")
    energy_consumption = models.FloatField(help_text="Energy consumption in kWh")
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, default="Unknown")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SmallCommercial(models.Model):
    name = models.CharField(max_length=255)
    energy_consumption = models.FloatField(help_text="Energy consumption in kWh")
    solar_generation = models.FloatField(help_text="Solar energy generated in kWh")
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
