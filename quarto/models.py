from django.db import models

from categoria.models import Categoria


class Quarto(models.Model):
    descricao = models.CharField("Descrição", max_length=100)
    idcategoria = models.ForeignKey(
        Categoria, verbose_name="Categoria", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.descricao)
