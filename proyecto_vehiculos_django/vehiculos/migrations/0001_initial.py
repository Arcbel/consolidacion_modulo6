# Generated by Django 4.2.2 on 2023-07-13 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(choices=[('Toyota', 'Toyota'), ('Ford', 'Ford'), ('Chevrolet', 'Chevrolet'), ('Honda', 'Honda'), ('Nissan', 'Nissan'), ('Fiat', 'Fiat')], default='Fiat', max_length=20)),
                ('modelo', models.CharField(max_length=100)),
                ('serial_carroceria', models.CharField(max_length=50)),
                ('serial_motor', models.CharField(max_length=50)),
                ('categoria', models.CharField(choices=[('P', 'Particular'), ('T', 'Transporte'), ('C', 'Carga')], default='P', max_length=20)),
                ('precio', models.FloatField()),
                ('fecha_creacion', models.DateField()),
                ('fecha_modificacion', models.DateField()),
            ],
        ),
    ]
