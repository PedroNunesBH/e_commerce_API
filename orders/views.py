from rest_framework import generics
from rest_framework import views
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.db.models import Sum
from .models import Order
from .serializers import OrderSerializer


class ListOrdersView(generics.ListAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer


class CreateOrdersView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():  # Verifica se o serializer é valido
            products_list = serializer.validated_data.get('products')  # Captura o valor(es) de products do serializer
            product_quantity_list = serializer.validated_data.get('each_product_quantity')
            error_warnings = []  # Cria uma lista vazia para armazenar msgs de erros caso haja
            for product in products_list:
                quantidade_do_produto = product_quantity_list[f"{product.pk}"]  # Captura a qtd do produto atraves do id
                if product.units < quantidade_do_produto:  # Verifica se tem a quantidade no estoque
                    error_warnings.append(f"Não há estoque suficiente para o produto {product.name}. ID : {product.id}")
            if error_warnings:
                return Response({"errors": error_warnings},
                                status=status.HTTP_400_BAD_REQUEST)  # Retorna as mensagens de erros e o codigo 400
            for product in products_list:
                quantidade_do_produto = product_quantity_list[f"{product.pk}"]  # Acessa novamente a qtd do produto
                product.units -= quantidade_do_produto  # Diminui a quantidade em estoque
                product.save()  # Salva no bd
            serializer.save()  # Cria o pedido Order
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)  # Retorna o json e o codigo 201 de criado com sucesso
        return super().post(request)


class DetailUpdateAndDestroyOrdersView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer


class TotalOrderBilling(views.APIView):  # View responsavel por calcular o faturamento total de pedidos
    permission_classes = (IsAdminUser,)  # Restringe para apenas administradores

    def get(self, request):
        total_billing = Order.objects.aggregate(
            Sum('total_price'))['total_price__sum']  # Soma todos os registros de total_price do model Order
        return JsonResponse({"total_billing": total_billing})
