# Generated by Django 4.2.2 on 2023-07-19 00:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehiculos', '0002_alter_vehiculo_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiculo',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
