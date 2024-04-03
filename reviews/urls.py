from django.urls import path
from .views import ListAndCreateReviewsView, DetailUpdateAndDestroyProductReviewView

urlpatterns = [
    path('reviews/', ListAndCreateReviewsView.as_view(), name="list_and_create_reviews"),
    path('review/<int:pk>', DetailUpdateAndDestroyProductReviewView.as_view(), name="review_pk"),
]
