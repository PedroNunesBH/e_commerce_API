from django.shortcuts import get_object_or_404
from rest_framework import views, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from reviews.models import ProductReview
from .models import Product
from .serializers import ProductSerializer
from reviews.serializers import ProductReviewSerializer


class ListAndCreateProductsView(generics.ListCreateAPIView):
    queryset = Product.objects.all()  # Define queryset como todos os objetos do model Product
    serializer_class = ProductSerializer  # classe do serializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class DetailUpdateAndDestroyProductsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()  # Define queryset como todos os objetos do model Product
    permission_classes = (IsAuthenticatedOrReadOnly,)  # Apenas autenticados podem metodo além do GET
    serializer_class = ProductSerializer


class ListReviewByProductView(generics.ListAPIView):
    serializer_class = ProductReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']  # Captura o pk do endpoint
        product_pk = get_object_or_404(Product, id=pk)  # Captura o objeto ou devolve 404
        product_reviews = ProductReview.objects.filter(product=product_pk)  # Captura todas as reviews do produto
        return product_reviews
