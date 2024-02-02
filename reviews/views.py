from rest_framework import generics
from .models import ProductReview
from .serializers import ProductReviewSerializer


class ListProductReviewView(generics.ListAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class CreateProductReviewView(generics.CreateAPIView):
    serializer_class = ProductReviewSerializer


class DetailUpdateAndDestroyProductReviewView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class ListReviewByProductView(generics.ListAPIView):
    serializer_class = ProductReviewSerializer

    def get_queryset(self):
        product_pk = self.kwargs['pk']  # Captura o produto
        product_reviews = ProductReview.objects.filter(product=product_pk)  # Captura todas as reviews do produto
        return product_reviews
