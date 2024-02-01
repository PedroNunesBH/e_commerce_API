"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import ListProductsView, CreateProductsView, DetailUpdateAndDestroyProductsView
from clients.views import ListClientsView, CreateClientsView, DetailUpdateAndDestroyClientsView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', ListProductsView.as_view(), name='products_list'),
    path('create_product/', CreateProductsView.as_view(), name='products_create'),
    path('product/<int:pk>', DetailUpdateAndDestroyProductsView.as_view(), name='product_pk'),

    path('clients/', ListClientsView.as_view(), name='clients_list'),
    path('create_client/', CreateClientsView.as_view(), name='clientes_create'),
    path('client/<int:pk>', DetailUpdateAndDestroyClientsView.as_view(), name='client_pk'),
]
