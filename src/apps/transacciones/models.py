from django.db import models
from django.utils import timezone

from apps.cuentas.models import Cuenta
from apps.motivos.models import Motivo


class Transaccion(models.Model):
    TIPO_CHOICES = [
        ('ingreso', 'Ingreso'),
        ('transferencia', 'Transferencia'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='transferencia')
    emisor = models.ForeignKey(
        'cuentas.Cuenta',  # Referencia completa a la app y el modelo
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='transacciones_emitidas'
    )
    receptor = models.ForeignKey(
        'cuentas.Cuenta',  # Referencia completa a la app y el modelo
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='transacciones_recibidas'
    )
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    motivo = models.ForeignKey(Motivo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - ${self.monto}"