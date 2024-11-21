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

