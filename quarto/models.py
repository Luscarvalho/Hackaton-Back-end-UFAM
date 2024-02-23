from django.db import models

from categoria.models import Categoria


class Quarto(models.Model):
    descricao = models.CharField(max_length=100)
    idcategoria = models.ForeignKey(
        Categoria, on_delete=models.CASCADE, null=True, blank=True)
