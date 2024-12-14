# Generated by Django 5.1.2 on 2024-12-13 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motivos', '0001_initial'),
        ('transacciones', '0002_transaccion_tipo_alter_transaccion_emisor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaccion',
            name='motivo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='motivos.motivo', default=1),
        ),
    ]
