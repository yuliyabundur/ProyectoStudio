from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio),
    path('especialistas/', especialistas),
    path('servicios/', servicios),
    path('clientes/', clientes),
    path('pedir-Cita/', pedir_cita),
]