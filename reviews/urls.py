from django.urls import path
from .views import ListProductReviewView, CreateProductReviewView, DetailUpdateAndDestroyProductReviewView

urlpatterns = [
    path('reviews/', ListProductReviewView.as_view(), name="reviews_list"),
    path('create_review/', CreateProductReviewView.as_view(), name="reviews_create"),
    path('review/<int:pk>', DetailUpdateAndDestroyProductReviewView.as_view(), name="review_pk"),
]
