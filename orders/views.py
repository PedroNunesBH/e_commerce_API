from rest_framework import generics
from rest_framework import views
from django.http import JsonResponse
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from .models import Order, PaymentMethod
from .serializers import OrderSerializer, PaymentMethodSerializer
from products.views import Product
from products.serializers import ProductSerializer


class ListOrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreateOrdersView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class DetailUpdateAndDestroyOrdersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreatePaymentMethodsView(generics.CreateAPIView):
    serializer_class = PaymentMethodSerializer


class TotalOrderBilling(views.APIView):  # View responsavel por calcular o faturamento total de pedidos
    def get(self, request):
        total_billing = Order.objects.aggregate(
                        Sum('total_price'))['total_price__sum']  # Soma todos os registros de total_price do model Order
        return JsonResponse({"total_billing": total_billing})


class DetailsPaymentMethodsView(views.APIView):
    def get(self, request):
        queryset = Order.objects.all()
        data = {"PIX": 0, "Dinheiro": 0, "Boleto": 0, "Cartão de Crédito": 0}
        for order in queryset:
            data[order.payment_method] += order.total_price
        return JsonResponse(data)


class DetailPaymentMethodView(views.APIView):  # View que retorna detalhes de metodo de pagamento
    def get(self, request, pk):
        method = get_object_or_404(PaymentMethod, id=pk)
        queryset = Order.objects.filter(payment_method=method)  # Filtra os pedidos do metodo de pagamento
        order_total_numbers = queryset.count()
        total_billing = queryset.aggregate(Sum('total_price'))['total_price__sum']  # Soma dos campos total_price
        data = {"name": method.method_name, "Total_orders": order_total_numbers, "Total billing": total_billing}
        return JsonResponse(data)
