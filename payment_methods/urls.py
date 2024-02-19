from django.urls import path
from .views import (ListPaymentMethodsView, CreatePaymentMethodsView, DetailUpdateAndDestroyPaymentMethodsView,
                    BillingStaticsPaymentMethodsView, GeneralPaymentMethodStatisticsView)

urlpatterns = [
    path('payment_methods/', ListPaymentMethodsView.as_view(), name='payment_methods_list'),
    path('create_payment_method/', CreatePaymentMethodsView.as_view(), name="payment_methods_create"),
    path('payment_method/<int:pk>/', DetailUpdateAndDestroyPaymentMethodsView.as_view(), name='payment_method_pk'),
    path('payment_methods_billing/', BillingStaticsPaymentMethodsView.as_view(),
         name="billing_statics_payment_method"),  # Exibe o faturamento total de todos os metodos de pagamentos
    path('payment_method_detail/<int:pk>', GeneralPaymentMethodStatisticsView.as_view(),
         name="general_statics_payment_method")  # Exibe estasticas do metodo de pagamento especificado na url
]
