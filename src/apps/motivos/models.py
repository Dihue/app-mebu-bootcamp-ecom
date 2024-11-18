from django.db import models


class Motivo(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.TextField()

    class Meta:
        managed = False
        db_table = 'motivo'
