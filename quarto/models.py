from django.db import models

from categoria.models import Categoria


class Quarto(models.Model):
    id_quarto = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)
    idcategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True, blank=True)
