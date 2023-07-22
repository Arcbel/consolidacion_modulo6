from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth.models import Permission


def index(request):
    return render(request, 'index.html', context={})

@permission_required('vehiculos.add_vehiculo')
def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/vehiculos/list')
    else:
        form = VehiculoForm()
        return render(request, 'add_vehiculo.html', {'form': form})

@login_required
def list_vehiculo(request):
    vehiculos = Vehiculo.objects.all()
    context = {'vehiculos': vehiculos}
    return render(request, 'list_vehiculo.html', context)
