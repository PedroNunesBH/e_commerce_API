from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

urlpatterns = [
    path('authentication/get_token/', TokenObtainPairView.as_view(), name='get_token'),
    path('authentication/verify_token/', TokenVerifyView.as_view(), name="verify_token")
]
