from rest_framework import serializers
from apps.orders.models import Orders

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['company', 'address', 'cargo_weight', 'cargo_size', 'eta', 'uuid']