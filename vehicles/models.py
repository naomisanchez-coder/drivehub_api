from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='vehicles')

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"