from django.db import models


class Motivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.descripcion}'
