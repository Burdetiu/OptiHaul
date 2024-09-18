from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    STATUS = (
        ('employee', 'employee'),
        ('manager', 'manager'),
    )

    is_manager = models.BooleanField(default=True)
    is_employee = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    status = models.CharField(max_length=100, choices=STATUS, default='manager')
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')

    def __str__(self):
        return self.username
    

