# Generated by Django 4.2.2 on 2023-07-16 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehiculos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vehiculo',
            name='fecha_modificacion',
            field=models.DateField(auto_now=True),
        ),
    ]