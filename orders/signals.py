from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Order


@receiver(m2m_changed, sender=Order.products.through)
def calculate_price(sender, instance, action, **kwargs):  # Funcao responsavel por calcular o preco do pedido
    if action in ('post_add', 'post_remove', 'post_clear'):  # Chama o signal caso a acao seja uma das 3
        total_price = [product.price for product in instance.products.all()] # Caclula o preco total somando os produtos do pedido
        total_price = sum(total_price)
        if instance.total_price != total_price:  # Verifica se o total_price é diferente do total_price do objeto
            instance.total_price = total_price  # Se for atribui o novo valor para total_price
            instance.save()  # Salva no bd
