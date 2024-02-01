from django.contrib import admin
from .models import ProductReview


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductReview._meta.fields]
    search_fields = ('user',)


admin.site.register(ProductReview, ProductReviewAdmin)
