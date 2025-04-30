from django.db import models

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=15, unique=True, verbose_name="Patente")
    brand = models.CharField(max_length=50, verbose_name="Marca")
    model = models.CharField(max_length=50, verbose_name="Modelo")
    year = models.PositiveIntegerField(verbose_name="Año")
    owner_name = models.CharField(max_length=100, verbose_name="Nombre del propietario")
    owner_phone = models.CharField(max_length=20, verbose_name="Teléfono del propietario")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.license_plate} - {self.brand} {self.model}"

class RepairRecord(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name="repairs", verbose_name="Vehículo")
    date = models.DateField(verbose_name="Fecha de reparación")
    description = models.TextField(verbose_name="Descripción de la reparación")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reparación {self.id} - {self.vehicle.license_plate} - {self.date}"
