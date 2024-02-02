from django.urls import path
from .views import CreatePaymentMethodsView, DetailsPaymentMethodsView, DetailPaymentMethodView
urlpatterns = [
    path('create_payment_method/', CreatePaymentMethodsView.as_view(), name="payment_methods_create"),

    path('payment_methods_billing/', DetailsPaymentMethodsView.as_view(),
         name="payment_methods"),  # Responsavel por devolver o faturamento total de cada método de pagamento
    path('payment_method_detail/<int:pk>', DetailPaymentMethodView.as_view(), name="detail_payment_method")
]