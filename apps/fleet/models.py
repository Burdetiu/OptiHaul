from django.conf import settings
from django.db import models

class Trucks(models.Model):
    registration_plate = models.CharField(max_length=30)
    truck_make = models.CharField(max_length=30)
    truck_model = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    truck_image = models.ImageField(null=True, blank=True, upload_to='media/truck-images/')
    status = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trucks_created')



class Trailers(models.Model):
    registration_plate = models.CharField(max_length=30)
    trailer_make = models.CharField(max_length=30)
    trailer_model = models.CharField(max_length=30)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=20)
    trailer_image = models.ImageField(null=True, blank=True, upload_to='media/trailer-images/')
    status = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trailers_created')
    
