from rest_framework import serializers
from django.db.models import Avg
from .models import Product
from reviews.models import ProductReview


class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField(read_only=True)  # Cria o campo calculado average_rating

    class Meta:
        model = Product  # Model associado
        fields = "__all__"  # Campos do modelo

    def get_average_rating(self, obj):  # Calcula o campo average_rating
        result = (ProductReview.objects.filter
                  (product=obj).aggregate(average_rating=Avg('note'))['average_rating'])  # Calcula a media das avaliacoes de cada produto
        if result:
            return f"{result:.2f}"  # Retorna a media caso exista avaliacoes com 2 casas decimais
        else:
            return "Não contém avaliações"  # Retorna essa string caso o produto não tenha nenhuma avaliação

