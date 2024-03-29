from django.db import models
from clients.models import Client
from products.models import Product


class ProductReview(models.Model):
    user = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='user_review')  # Autor do review
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name="product_review")  # Produtor referente
    note = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"Usuário : {self.user.username} - Avaliação de {self.product.name}"
