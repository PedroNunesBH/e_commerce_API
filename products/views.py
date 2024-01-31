from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ListProductsView(generics.ListAPIView):  # View para listar objetos do model
    queryset = Product.objects.all()  # Define queryset como todos os objetos do model Product
    serializer_class = ProductSerializer

