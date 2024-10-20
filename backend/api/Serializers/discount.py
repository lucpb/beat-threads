from rest_framework import serializers
from ..models import Discount

class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        product = Discount