from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('especialistas/', especialistas, name='especialistas'),
    path('servicios/', servicios, name='servicios'),
    path('clientes/', clientes, name='clientes'),
    path('pedir-cita/', pedir_cita, name='pedir-cita'),
    #path('especialistas-formulario/', especialistas_formulario, name='especialistas-formulario'),
    path('servicios-formulario/', servicios_formulario, name='servicios-formulario'),
    path('clientes-formulario/', clientes_formulario, name='clientes-formulario'),
    path('pedir-cita-formulario/', citas_formulario, name='pedir-cita-formulario'),
    #path('busqueda-especialista/', busqueda_especialista, name='busqueda-especialista'),
    path('buscar/', buscar, name='buscar'),
    path('leer-servicios/', leer_servicios, name='leer-servicios'),
    path('eliminar-servicios/<servicio_id>', eliminar_servicio, name='eliminar-servicios'),
    path('editar-servicios/<servicio_id>', editar_servicio, name='editar-servicios'),
    path('especialistas-list', EspecialistaList.as_view(), name='especialistas-list'),
    path('especialistas-detalle/<pk>', EspecialistaDetail.as_view(), name='especialistas-detalle'),
    path('especialistas-nuevo/', EspecialistaCreacion.as_view(), name='especialistas-nuevo'),
    path('especialistas-editar/<pk>', EspecialistaUpdate.as_view(), name='especialistas-editar'),
    path('especialistas-eliminar/<pk>', EspecialistaDelete.as_view(), name='especialistas-eliminar'),
    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout', LogoutView.as_view(template_name='AppBeautyStudio/logout.html'), name='logout'),
    path('editar-perfil/', editar_perfil, name='editar-perfil'),
    path('editar-avatar/', editar_avatar, name='editar-avatar'),
]