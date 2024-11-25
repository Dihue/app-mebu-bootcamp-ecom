from django.conf import settings
from django.db import models

from apps.usuarios.models import Usuario


ESTADO_CHOICES = [
        (True, 'Activo'),
        (False, 'Inactivo')
]


class Cuenta(models.Model):
	id = models.BigAutoField(primary_key=True)
	saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0)
	estado = models.BooleanField(choices=ESTADO_CHOICES, default=True)
	usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.id} - {self.usuario}'


class CuentaFrecuente(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)
    alias = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        unique_together = ('usuario', 'cuenta')

    def __str__(self):
        return f'{self.usuario.username} - {self.cuenta.usuario.username} (Frecuente)'
