from rest_framework import serializers
from ..models import Product, Category, Inventory, ProductReview

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        product = Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        product = Category

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        product = Inventory

class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        product = ProductReview