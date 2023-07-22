from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Vehiculo(models.Model):
    MARCAS = (
        ('Toyota', 'Toyota'),
        ('Ford','Ford'),
        ('Chevrolet','Chevrolet'),
        ('Honda','Honda'),
        ('Nissan','Nissan'),
        ('Fiat','Fiat')
    )
    marca = models.CharField(max_length=20, choices=MARCAS, default='Fiat')

    modelo = models.CharField(max_length=100)

    serial_carroceria = models.CharField(max_length=50)

    serial_motor = models.CharField(max_length=50)

    CATEGORIAS = (
        ('P', 'Particular'),
        ('T', 'Transporte'),
        ('C', 'Carga')
    )

    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='P')

    precio = models.FloatField()

    fecha_creacion = models.DateField(auto_now_add=True)

    fecha_modificacion = models.DateField(auto_now=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)


    def get_absoluted_url(self):
        return reverse ('Vehiculo', args=[1945])

    def __str__(self) -> str:
        pass
