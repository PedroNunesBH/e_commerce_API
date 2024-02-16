from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

urlpatterns = [
    path('authentication/get_token/', TokenObtainPairView.as_view(), name='get_token'),
    path('authentication/verify_token/', TokenVerifyView.as_view(), name="verify_token"),
    path('authentication/refresh_token/', TokenRefreshView.as_view(), name='refresh_token')
]
