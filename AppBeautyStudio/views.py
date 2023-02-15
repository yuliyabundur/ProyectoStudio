from django.shortcuts import render
from django.http import HttpResponse

#from AppBeautyStudio.models import Especialistas

# Create your views here.
def inicio(request):
    return HttpResponse('Vista inicio')

def especialistas(request):
    return HttpResponse('Vista especialistas')

def servicios(request):
    return HttpResponse('Vista servicios')

def clientes(request):
    return HttpResponse('Vista clientes')

def pedir_cita(request):
    return HttpResponse('Vista Pedir cita')
