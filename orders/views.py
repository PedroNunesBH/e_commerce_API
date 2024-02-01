from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer


class ListOrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreateOrdersView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class DetailUpdateAndDestroyOrdersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

