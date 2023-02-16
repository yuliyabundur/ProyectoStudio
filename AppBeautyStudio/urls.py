from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('especialistas/', especialistas, name='especialistas'),
    path('servicios/', servicios, name='servicios'),
    path('clientes/', clientes, name='clientes'),
    path('pedir-cita/', pedir_cita, name='pedir-cita'),
]