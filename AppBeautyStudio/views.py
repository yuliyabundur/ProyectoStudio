from django.shortcuts import render, redirect

from .models import Especialista, Servicio, Cliente
from .forms import EspecialistaFormulario, ServicioFormulario, ClienteFormulario


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

    mi_formulario = EspecialistaFormulario ()
    return render(request, 'AppBeautyStudio/Especialistas-formulario.html',{'formulario_especialistas': mi_formulario})

def servicios_formulario(request):

    if request.method == 'POST':
        nuevo_servicio = Servicio(servicio=request.POST['servicio'], precio=request.POST['precio'])
        nuevo_servicio.save()
        return redirect('servicios-formulario')

    mi_formulario = ServicioFormulario ()
    return render(request, 'AppBeautyStudio/Servicios-formulario.html',{'formulario_servicios': mi_formulario})

def clientes_formulario(request):

    if request.method == 'POST':
        nuevo_cliente = Cliente(nombre=request.POST['nombre'], apellidos=request.POST['apellidos'], telefono=request.POST['telefono'], email=request.POST['email'])
        nuevo_cliente.save()
        return redirect('clientes-formulario')

    mi_formulario = ClienteFormulario ()
    return render(request, 'AppBeautyStudio/Clientes-formulario.html',{'formulario_clientes': mi_formulario})

