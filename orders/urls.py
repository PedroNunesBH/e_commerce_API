from django.urls import path
from .views import (ListOrdersView, CreateOrdersView, DetailUpdateAndDestroyOrdersView, TotalOrderBilling,
                    DetailsPaymentMethodsView, DetailPaymentMethodView, CreatePaymentMethodsView)

urlpatterns = [
    path('orders/', ListOrdersView.as_view(), name="orders_list"),
    path('create_order/', CreateOrdersView.as_view(), name="orders_create"),
    path('order/<int:pk>', DetailUpdateAndDestroyOrdersView.as_view(), name="orders_pk"),

    path('create_payment_method/', CreatePaymentMethodsView.as_view(), name="payment_methods_create"),

    path('total_billing/', TotalOrderBilling.as_view(), name="total_billing"),  # Total de faturamento de pedidos

    path('payment_methods_billing/', DetailsPaymentMethodsView.as_view(),
         name="payment_methods"),  # Responsavel por devolver o faturamento total de cada método de pagamento
    path('payment_method_detail/<int:pk>', DetailPaymentMethodView.as_view(), name="detail_payment_method")
]
