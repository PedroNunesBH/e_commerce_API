from django.urls import path
from .views import (ListAndCreateProductsView, DetailUpdateAndDestroyProductsView,
                    ListReviewByProductView)

urlpatterns = [
    path('products/', ListAndCreateProductsView.as_view(), name="list_and_create_products"),
    path('product/<int:pk>', DetailUpdateAndDestroyProductsView.as_view(), name="product_pk"),
    path('product_reviews/<int:pk>', ListReviewByProductView.as_view(), name="products_reviews")
]
