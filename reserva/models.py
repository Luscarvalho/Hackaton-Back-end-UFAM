from django.db import models
from django.contrib.auth.models import User

from quarto.models import Quarto


class Reserva(models.Model):
    dt_inicial = models.DateField("Data inicial")
    dt_final = models.DateField("Data final")
    idclient = models.ForeignKey(User, verbose_name="Cliente", on_delete=models.CASCADE, null=True, blank=True)
    idquarto = models.ForeignKey(Quarto, verbose_name="Quarto", on_delete=models.CASCADE, null=True, blank=True)
