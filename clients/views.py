from django.shortcuts import render
from rest_framework import generics
from .models import Client
from .serializers import ClientSerializer


class ListClientsView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class CreateClientsView(generics.CreateAPIView):
    serializer_class = ClientSerializer


class DetailUpdateAndDestroyClientsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
