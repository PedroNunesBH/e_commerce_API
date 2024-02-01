from django.contrib import admin
from .models import Client


class ClientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Client._meta.fields]
    search_fields = ('name',)


admin.site.register(Client, ClientAdmin)
