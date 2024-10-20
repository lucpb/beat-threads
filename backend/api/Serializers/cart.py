from rest_framework import serializers
from ..models import ShoppingCart, Wishlist

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        product = ShoppingCart

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        product = Wishlist