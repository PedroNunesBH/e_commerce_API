from django.urls import path
from .views import (CreatePaymentMethodsView, DetailsPaymentMethodsView, DetailPaymentMethodView,
                    DetailUpdateAndDestroyPaymentMethodsView, ListPaymentMethodsView)
urlpatterns = [
    path('payment_methods/', ListPaymentMethodsView.as_view(), name='payment_methods_list'),
    path('create_payment_method/', CreatePaymentMethodsView.as_view(), name="payment_methods_create"),
    path('payment_method/<int:pk>/', DetailUpdateAndDestroyPaymentMethodsView.as_view(), name='payment_method_pk'),
    path('payment_methods_billing/', DetailsPaymentMethodsView.as_view(),
         name="payment_methods"),  # Responsavel por devolver o faturamento total de cada método de pagamento
    path('payment_method_detail/<int:pk>', DetailPaymentMethodView.as_view(), name="detail_payment_method")
]
