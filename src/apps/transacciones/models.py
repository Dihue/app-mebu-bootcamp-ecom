from django.db import models
from django.utils import timezone

from apps.cuentas.models import Cuenta
from apps.motivos.models import Motivo


class Transaccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    emisor = models.ForeignKey(Cuenta, blank=True, null=True, on_delete=models.CASCADE)
    receptor = models.ForeignKey(Cuenta, related_name='transaccion_receptor_set', blank=True, null=True, on_delete=models.CASCADE)
    motivo = models.ForeignKey(Motivo, blank=True, null=True, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateField(default=timezone.now)
