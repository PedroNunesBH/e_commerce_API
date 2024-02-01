from django.contrib import admin
from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    search_fields = ('pk',)


admin.site.register(Order, OrderAdmin)
