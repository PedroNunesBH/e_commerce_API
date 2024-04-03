from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import ProductReview
from .serializers import ProductReviewSerializer


class ListAndCreateReviewsView(generics.ListCreateAPIView):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )  # Apenas autenticados podem criar(metodo POST) uma review


class DetailUpdateAndDestroyProductReviewView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductReview.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ProductReviewSerializer
