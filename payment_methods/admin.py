from django.contrib import admin
from .models import PaymentMethod


class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PaymentMethod._meta.fields]
    search_fields = ('method_name', )


admin.site.register(PaymentMethod, PaymentMethodAdmin)
