from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('especialistas/', especialistas, name='especialistas'),
    path('servicios/', servicios, name='servicios'),
    path('clientes/', clientes, name='clientes'),
    path('pedir-cita/', pedir_cita, name='pedir-cita'),
    path('especialistas-formulario/', especialistas_formulario, name='especialistas-formulario'),
    path('servicios-formulario/', servicios_formulario, name='servicios-formulario'),
    path('clientes-formulario/', clientes_formulario, name='clientes-formulario'),
    path('pedir-cita-formulario/', citas_formulario, name='pedir-cita-formulario'),
]