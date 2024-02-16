from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import ProductReview
from .serializers import ProductReviewSerializer


class ListProductReviewView(generics.ListAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class CreateProductReviewView(generics.CreateAPIView):
    serializer_class = ProductReviewSerializer
    permission_classes = (IsAuthenticated,)  # Apenas autenticados podem criar uma review


class DetailUpdateAndDestroyProductReviewView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductReviewSerializer
