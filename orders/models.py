from django.db import models
from clients.models import Client
from products.models import Product
from payment_methods.models import PaymentMethod


class Order(models.Model):
    client = models.ForeignKey(Client,
                               on_delete=models.PROTECT,
                               related_name="client_order")  # Cliente que efetuou o pedido
    products = models.ManyToManyField(Product, related_name='products_order')  # Produtos do pedido
    date = models.DateTimeField(auto_now_add=True)  # Preenchimento da data e hora automático
    total_price = models.FloatField(default=0.0)
    address_to_delivery = models.TextField()
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    each_product_quantity = models.JSONField()  # Recebe uma lista de inteiros com a quantidade de cada produto

    def __str__(self):
        return self.pk  # Retorna o código da venda(id/pk)
