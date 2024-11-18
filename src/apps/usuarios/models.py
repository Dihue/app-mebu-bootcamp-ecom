from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
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
    
    def __str__(self):
        return f'{self.username}'
