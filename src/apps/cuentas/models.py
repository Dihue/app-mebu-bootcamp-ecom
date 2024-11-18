from django.db import models

from apps.usuarios.models import Usuario

class Cuenta(models.Model):
    id = models.BigAutoField(primary_key=True)
    saldo = models.DecimalField(max_digits=65535, decimal_places=65535)
    estado = models.TextField()
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cuenta'
