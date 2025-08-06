from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='produtos')
    
    def __str__(self):
        return self.nome