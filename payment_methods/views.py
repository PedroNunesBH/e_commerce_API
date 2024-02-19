from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum
from rest_framework import views, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from orders.models import Order
from .serializers import PaymentMethodSerializer
from .models import PaymentMethod


class ListPaymentMethodsView(generics.ListAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class CreatePaymentMethodsView(generics.CreateAPIView):
    serializer_class = PaymentMethodSerializer
    permission_classes = (IsAdminUser,)  # Apenas para usuarios administradores


class DetailUpdateAndDestroyPaymentMethodsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )  # Usuarios nao autenticados podem ver o get(detail) apenas


class BillingStaticsPaymentMethodsView(views.APIView):  # Exibe o faturamento de cada metodo de pagamento
    permission_classes = (IsAdminUser,)

    def get(self, request):
        queryset = Order.objects.all()
        data = {"Pix": 0, "Dinheiro": 0, "Boleto Bancário": 0, "Cartão de Crédito": 0}
        for order in queryset:
            data[order.payment_method.method_name] += order.total_price  # Adiciona o valor total de cada pedido
        for key, total in data.items():
            data[key] = round(total, 2)  # Arredonda o total de cada metodo de pagamento para duas casas
        print(data)
        return JsonResponse(data)


class GeneralPaymentMethodStatisticsView(views.APIView):  # View que retorna detalhes do metodo de pagamento especificado na url
    permission_classes = (IsAdminUser,)

    def get(self, request, pk):
        method = get_object_or_404(PaymentMethod, id=pk)
        queryset = Order.objects.filter(payment_method=method)  # Filtra os pedidos do metodo de pagamento
        order_total_numbers = queryset.count()
        total_billing = queryset.aggregate(Sum('total_price'))['total_price__sum']  # Soma dos campos total_price
        data = {"name": method.method_name, "Total_orders": order_total_numbers, "Total billing": total_billing}
        for chave, valor in data.items():
            data["Total billing"] = f"{total_billing:.2f}"
        return JsonResponse(data)
