from django.shortcuts import render
from rest_framework import generics
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
