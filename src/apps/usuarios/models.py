from django.db import models

from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    dni = models.IntegerField(unique=True, null=True)
    es_admin = models.BooleanField(default=False)
    foto_perfil = models.ImageField(upload_to='avatars/', null=True, blank=True)
    

    def __str__(self):
        return f'{self.username}'
