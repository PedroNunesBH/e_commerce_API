from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()  # Define que o campo total_price apareca somenete em GET

    class Meta:
        model = Order
        fields = "__all__"
