from django.contrib import admin
from .models import Vehiculo

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo','categoria', 'precio')

admin.site.register(Vehiculo, VehiculoAdmin)
