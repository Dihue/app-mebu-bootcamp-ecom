# Generated by Django 5.1.2 on 2024-11-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Motivo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
