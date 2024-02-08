from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import views, generics
from reviews.models import ProductReview
from .models import Product
from .serializers import ProductSerializer


class ListProductsView(generics.ListAPIView):  # View para listar objetos do model
    queryset = Product.objects.all()  # Define queryset como todos os objetos do model Product
    serializer_class = ProductSerializer  # classe do serializer


class CreateProductsView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class DetailUpdateAndDestroyProductsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()  # Define queryset como todos os objetos do model Product
    serializer_class = ProductSerializer


class ProductReviews(views.APIView):  # Busca todas as avaliacoes de um produto especifico
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)  # Captura o produto atraves da pk
        reviews = ProductReview.objects.filter(product=product)  # Busca todas reviews do produto especifico
        data_reviews = [{'id': review.id, 'description': review.description, 'rating': review.note,
                         "autor": review.user.username} for review in reviews]
        return JsonResponse(data_reviews, safe=False)
