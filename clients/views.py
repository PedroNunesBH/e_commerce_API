from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Client
from .serializers import ClientSerializer


class ListAndCreateClientsView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    permission_classes = (IsAuthenticated,)  # Restringe a view apenas para usuarios autenticados
    serializer_class = ClientSerializer


class DetailUpdateAndDestroyClientsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ClientSerializer
