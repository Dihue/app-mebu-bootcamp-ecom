# Generated by Django 5.1.2 on 2024-11-25 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('estado', models.BooleanField(choices=[(True, 'Activo'), (False, 'Inactivo')], default=True)),
            ],
        ),
        migrations.CreateModel(
            name='CuentaFrecuente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
