from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import views
from orders.models import Order
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from rest_framework import generics
from .serializers import PaymentMethodSerializer
from .models import PaymentMethod


class CreatePaymentMethodsView(generics.CreateAPIView):
    serializer_class = PaymentMethodSerializer


class DetailsPaymentMethodsView(views.APIView):
    def get(self, request):
        queryset = Order.objects.all()
        data = {"Pix": 0, "Dinheiro": 0, "Boleto": 0, "Cartão de Crédito": 0}
        for order in queryset:
            method_name = order.payment_method.method_name
            data[method_name] += order.total_price
        return JsonResponse(data)


class DetailPaymentMethodView(views.APIView):  # View que retorna detalhes de metodo de pagamento
    def get(self, request, pk):
        method = get_object_or_404(PaymentMethod, id=pk)
        queryset = Order.objects.filter(payment_method=method)  # Filtra os pedidos do metodo de pagamento
        order_total_numbers = queryset.count()
        total_billing = queryset.aggregate(Sum('total_price'))['total_price__sum']  # Soma dos campos total_price
        data = {"name": method.method_name, "Total_orders": order_total_numbers, "Total billing": total_billing}
        return JsonResponse(data)
