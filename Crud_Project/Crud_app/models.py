from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=300)
