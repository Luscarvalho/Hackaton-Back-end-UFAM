from django.db import models
from django.contrib.auth.models import User

from quarto.models import Quarto


class Reserva(models.Model):
    dt_inicial = models.DateField()
    dt_final = models.DateField()
    idclient = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    idquarto = models.ForeignKey(Quarto, on_delete=models.CASCADE, null=True, blank=True)
