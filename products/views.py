from rest_framework import views, generics
from reviews.models import ProductReview
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
from reviews.serializers import ProductReviewSerializer


class ListProductsView(generics.ListAPIView):  # View para listar objetos do model
    queryset = Product.objects.all()  # Define queryset como todos os objetos do model Product
    serializer_class = ProductSerializer  # classe do serializer


class CreateProductsView(generics.CreateAPIView):
    serializer_class = ProductSerializer


class DetailUpdateAndDestroyProductsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()  # Define queryset como todos os objetos do model Product
    serializer_class = ProductSerializer


class ListReviewByProductView(generics.ListAPIView):
    serializer_class = ProductReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']  # Captura o pk do endpoint
        product_pk = get_object_or_404(Product, id=pk)  # Captura o objeto ou devolve 404
        product_reviews = ProductReview.objects.filter(product=product_pk)  # Captura todas as reviews do produto
        return product_reviews
