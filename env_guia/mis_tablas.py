# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.TextField(unique=True)
    nombre = models.TextField()
    apellido = models.TextField()
    dni = models.BigIntegerField(unique=True)
    email = models.TextField(unique=True)
    password = models.TextField()
    role = models.TextField()
    foto_perfil = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class Cuenta(models.Model):
    id = models.BigAutoField(primary_key=True)
    saldo = models.DecimalField(max_digits=65535, decimal_places=65535)
    estado = models.TextField()
    usuario = models.ForeignKey(Usuario, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cuenta'


class Motivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'motivo'


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



