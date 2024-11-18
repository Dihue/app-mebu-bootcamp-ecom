from django.db import models

from apps.cuentas.models import Cuenta
from apps.motivos.models import Motivo


class Transaccion(models.Model):
    id = models.BigAutoField(primary_key=True)
    emisor = models.ForeignKey(Cuenta, models.DO_NOTHING, blank=True, null=True)
    receptor = models.ForeignKey(Cuenta, models.DO_NOTHING, related_name='transaccion_receptor_set', blank=True, null=True)
    motivo = models.ForeignKey(Motivo, models.DO_NOTHING, blank=True, null=True)
    monto = models.DecimalField(max_digits=65535, decimal_places=65535)
    fecha = models.DateTimeField()
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = 'transaccion'
