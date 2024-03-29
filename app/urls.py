from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('products.urls')),
    path('api/v1/', include('clients.urls')),
    path('api/v1/', include('reviews.urls')),
    path('api/v1/', include('orders.urls')),
    path('api/v1/', include('payment_methods.urls')),
    path('api/v1/', include('authentication.urls'))
]
