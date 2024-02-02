from django.urls import path
from .views import ListOrdersView, CreateOrdersView, DetailUpdateAndDestroyOrdersView, TotalOrderBilling

urlpatterns = [
    path('orders/', ListOrdersView.as_view(), name="orders_list"),
    path('create_order/', CreateOrdersView.as_view(), name="orders_create"),
    path('order/<int:pk>', DetailUpdateAndDestroyOrdersView.as_view(), name="orders_pk"),

    path('total_billing/', TotalOrderBilling.as_view(), name="total_billing"),  # Total de faturamento de pedidos
]
