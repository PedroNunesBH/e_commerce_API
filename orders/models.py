from django.db import models
from clients.models import Client
from products.models import Product

PAYMENT_METHODS = (("Dinheiro", "Dinheiro"), ("Cartão de Crédito", "Cartão de Crédito"),
                   ("PIX", "PIX"), ("Boleto", "Boleto"))


class Order(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.PROTECT,
                               related_name="client_order")  # Cliente que efetuou o pedido
    products = models.ManyToManyField(Product, related_name='products_order')  # Produtos do pedido
    date = models.DateTimeField(auto_now_add=True)  # Preenchimento da data e hora automático
    total_price = models.FloatField()
    address_to_delivery = models.TextField()
    payment_method = models.CharField(max_length=30, choices=PAYMENT_METHODS, default="PIX")

    def __str__(self):
        return self.pk  # Retorna o código da venda(id/pk)


