from django.db import models


class Categoria(models.Model):
    descricao = models.CharField("Descrição", max_length=100)
    valor = models.DecimalField("Valor", max_digits=6, decimal_places=2)
    
    def __str__(self):
        return "{}".format(self.descricao)
