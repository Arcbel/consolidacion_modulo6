from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add_vehiculo),
    path('list', views.list_vehiculo)
]