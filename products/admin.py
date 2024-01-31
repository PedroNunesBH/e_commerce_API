from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'description', 'model', 'color', 'warrant_period')
    search_fields = ('name',)


admin.site.register(Product, ProductAdmin)
