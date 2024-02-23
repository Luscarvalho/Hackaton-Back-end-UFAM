from django.db import models

from quarto.models import Quarto
from cliente.models import Cliente


class Reserva(models.Model):
    dt_inicial = models.DateField("Data inicial")
    dt_final = models.DateField("Data final")
    idclient = models.ForeignKey(Cliente, verbose_name="Cliente", on_delete=models.CASCADE, null=True, blank=True)
    idquarto = models.ForeignKey(Quarto, verbose_name="Quarto", on_delete=models.CASCADE, null=True, blank=True)
