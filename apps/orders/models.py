import uuid
from django.conf import settings
from django.db import models


class Orders(models.Model):

    UNLOADING = 'unloading'
    LOADING = 'loading'
    ORDER_TYPE_CHOICES = [
        (UNLOADING, 'Unloading'),
        (LOADING, 'Loading'),
    ]

    company = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    cargo_weight = models.BigIntegerField()
    cargo_size = models.CharField(max_length=100)
    eta = models.DateField()
    status = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders_created'
    )
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE_CHOICES)

    
    def __str__(self):
        return str(self.uuid)