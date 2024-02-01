from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=150)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    warrant_period = models.CharField(max_length=100)
    units = models.PositiveIntegerField()

    def __str__(self):
        return self.name
