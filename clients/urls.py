from django.urls import path
from .views import ListClientsView, CreateClientsView, DetailUpdateAndDestroyClientsView

urlpatterns = [
    path('clients/', ListClientsView.as_view(), name='clients_list'),
    path('create_client/', CreateClientsView.as_view(), name='clients_create'),
    path('client/<int:pk>', DetailUpdateAndDestroyClientsView.as_view(), name='client_pk'),
]
