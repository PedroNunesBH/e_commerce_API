from django.urls import path
from .views import ListProductsView, CreateProductsView, DetailUpdateAndDestroyProductsView

urlpatterns = [
    path('products/', ListProductsView.as_view(), name='products_list'),
    path('create_product/', CreateProductsView.as_view(), name='products_create'),
    path('product/<int:pk>', DetailUpdateAndDestroyProductsView.as_view(), name='product_pk'),
]
