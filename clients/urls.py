from django.urls import path
from .views import ListAndCreateClientsView, DetailUpdateAndDestroyClientsView

urlpatterns = [
    path('clients/', ListAndCreateClientsView.as_view(), name='list_and_create_clients'),
    path('client/<int:pk>', DetailUpdateAndDestroyClientsView.as_view(), name='client_pk'),
]
