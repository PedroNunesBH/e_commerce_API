from django.shortcuts import render
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
