from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product  # Model associado
        fields = "__all__"  # Campos do modelo
