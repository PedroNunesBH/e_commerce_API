from django.urls import path
from .views import (ListAndCreateOrdersView, DetailUpdateAndDestroyOrdersView, TotalOrderBilling)

urlpatterns = [
    path('orders/', ListAndCreateOrdersView.as_view(), name="list_and_create_orders"),
    path('order/<int:pk>', DetailUpdateAndDestroyOrdersView.as_view(), name="orders_pk"),
    path('total_billing/', TotalOrderBilling.as_view(), name="total_billing"),  # Total de faturamento de pedidos
]
