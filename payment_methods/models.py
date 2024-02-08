from django.db import models


class PaymentMethod(models.Model):  # Tabela de métodos de pagamentos
    method_name = models.CharField(max_length=50)

    def __str__(self):
        return self.method_name
