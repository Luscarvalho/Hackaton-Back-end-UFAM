from django.db import models


class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
