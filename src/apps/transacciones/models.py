from django.db import models
from django.utils import timezone

from apps.cuentas.models import Cuenta
from apps.motivos.models import Motivo


class Transaccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    emisor = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='transferencias_emisor')
    receptor = models.ForeignKey(Cuenta, on_delete=models.CASCADE, related_name='transferencias_receptor')
    motivo = models.ForeignKey(Motivo, blank=True, null=True, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateField(default=timezone.now)

    def __str__(self):
        return f'Transferencia de {self.emisor} a {self.receptor} - $ {self.monto}'