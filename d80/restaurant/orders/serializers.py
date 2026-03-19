from rest_framework import serializers
from .models import Order, OrderInvoice

# This is the simplest implementation of OrderSerilizer
# where in Order related fields will be returned ONLY.
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

# This is the simplest implementation of OrderInvoiceSerilizer
# where in OrderInvoice related fields will be returned ONLY.
class OrderInvoiceSerializer(serializers.ModelSerializer):
    # Although DB table / model has created_at, response will be returned as generated_at
    generated_at = serializers.DateTimeField(source="created_at", read_only=True)

    class Meta:
        model = OrderInvoice
        fields = [
            "id",
            "generated_at",
            "invoice_number",
            "order",
        ]

"""
    This implemention reflects, how should we combine two models to return a JOINED data
    Order Model and MorderInvoice model is clubbed to return a comined data to VIEWS.
"""
class OrderWithInvoiceSerializer(serializers.ModelSerializer):
    invoice = OrderInvoiceSerializer(read_only=True)
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
            "invoice",
        ]