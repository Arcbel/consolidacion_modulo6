from django.contrib import admin
from django.urls import path, include
from vehiculos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('vehiculos/', include('vehiculos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
