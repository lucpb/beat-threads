from rest_framework import serializers
from ..models import Order, OrderItem, Payment, ShippingAddress

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        product = Order

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        product = OrderItem

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        product = Payment

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        product = ShippingAddress