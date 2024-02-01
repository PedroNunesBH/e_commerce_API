from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    cpf = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
