from django.shortcuts import render, redirect

from .models import Especialista


#from AppBeautyStudio.models import Especialistas

# Create your views here.
def inicio(request):
    return render(request,'AppBeautyStudio/Inicio.html')

def especialistas(request):
    return render(request,'AppBeautyStudio/Especialistas.html')

def servicios(request):
    return render(request,'AppBeautyStudio/Servicios.html')

def clientes(request):
    return render(request,'AppBeautyStudio/Clientes.html')

def pedir_cita(request):
    return render(request,'AppBeautyStudio/Pedir_Cita.html')

def especialistas_formulario(request):

    if request.method == 'POST':
        nuevo_especialista = Especialista(nombre=request.POST['nombre'], apellidos=request.POST['apellidos'], profesion=request.POST['profesion'])
        nuevo_especialista.save()
        return redirect('especialistas-formulario')

    return render(request, 'AppBeautyStudio/Especialistas-formulario.html')