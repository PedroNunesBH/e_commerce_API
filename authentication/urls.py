from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('authentication/get_token/', TokenObtainPairView.as_view(), name='get_token')
]
