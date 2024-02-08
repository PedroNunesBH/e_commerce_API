from rest_framework import generics
from rest_framework import views
from django.http import JsonResponse
from django.db.models import Sum
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


class TotalOrderBilling(views.APIView):  # View responsavel por calcular o faturamento total de pedidos
    def get(self, request):
        total_billing = Order.objects.aggregate(
                        Sum('total_price'))['total_price__sum']  # Soma todos os registros de total_price do model Order
        return JsonResponse({"total_billing": total_billing})
