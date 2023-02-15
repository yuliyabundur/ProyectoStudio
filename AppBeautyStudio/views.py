from django.shortcuts import render
from django.http import HttpResponse

from AppBeautyStudio.models import Especialistas

# Create your views here.
def especialistas(request):
    especialista = Especialistas(nombre='Anastasiya', apellidos='Gonzalez', profesion='cejas')
    especialista.save()
    respuesta = f'Nombre: {especialista.nombre}, Apellido: {especialista.apellidos}, Especialista: {especialista.profesion}, '

    return HttpResponse(respuesta)
