from rest_framework import serializers
from .models import Order

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "customer_name",
            "customer_phone",
            "total_amount",
            "status",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]