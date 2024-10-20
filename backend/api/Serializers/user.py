from rest_framework import serializers
from ..models import User, CustomerProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        product = User

class CustomerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        product = CustomerProfile