from django.shortcuts import render, redirect

from .models import Especialista, Servicio, Cliente, Cita
from .forms import EspecialistaFormulario, ServicioFormulario, ClienteFormulario, CitaFormulario


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

    #if request.method == 'POST':
    #   nuevo_especialista = Especialista(nombre=request.POST['nombre'], apellidos=request.POST['apellidos'], profesion=request.POST['profesion'])
    #   nuevo_especialista.save()
    #   return redirect('especialistas-formulario')

    if request.method == 'POST':
        mi_formulario = EspecialistaFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_especialista = Especialista(nombre=informacion['nombre'], apellidos=informacion['apellidos'], profesion=informacion['profesion'])
            nuevo_especialista.save()
            return redirect('especialistas-formulario')
      
    mi_formulario = EspecialistaFormulario 
    return render(request, 'AppBeautyStudio/Especialistas-formulario.html',{'formulario_especialistas': mi_formulario})

def servicios_formulario(request):

    #if request.method == 'POST':
        #nuevo_servicio = Servicio(servicio=request.POST['servicio'], precio=request.POST['precio'])
        #nuevo_servicio.save()
        #return redirect('servicios-formulario')

    if request.method == 'POST':
        mi_formulario = ServicioFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_servicio = Servicio(servicio=informacion['servicio'], precio=informacion['precio'])
            nuevo_servicio.save()
            return redirect('servicios-formulario')

    mi_formulario = ServicioFormulario
    return render(request, 'AppBeautyStudio/Servicios-formulario.html',{'formulario_servicios': mi_formulario})

def clientes_formulario(request):

    #if request.method == 'POST':
        #nuevo_cliente = Cliente(nombre=request.POST['nombre'], apellidos=request.POST# ['apellidos'], telefono=request.POST['telefono'], email=request.POST['email'])
        #nuevo_cliente.save()
        #return redirect('clientes-formulario')

    if request.method == 'POST':
         mi_formulario = ClienteFormulario(request.POST)

         if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nuevo_cliente = Cliente(nombre=informacion['nombre'], apellidos=informacion['apellidos'], telefono=informacion['telefono'], email=informacion['email'])
            nuevo_cliente.save()
            return redirect('clientes-formulario')

    mi_formulario = ClienteFormulario ()
    return render(request, 'AppBeautyStudio/Clientes-formulario.html',{'formulario_clientes': mi_formulario})

def citas_formulario(request):

    #if request.method == 'POST':
        #nueva_cita = Cita(apellidos_especialista=request.POST['apellidos_especialista'], fecha_cita=request.POST['fecha_cita'], reservado=request.POST['reservado'])
        #nueva_cita.save()
        #return redirect('clientes-formulario')

    if request.method == 'POST':
         mi_formulario = CitaFormulario(request.POST)

         if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            nueva_cita = Cita(apellidos_especialista=informacion['apellidos_especialista'], fecha_cita=informacion['fecha_cita'], reservado=informacion['reservado'])
            nueva_cita.save()
            return redirect('pedir-cita-formulario')

    mi_formulario = CitaFormulario ()
    return render(request, 'AppBeautyStudio/citas-formulario.html',{'formulario_citas': mi_formulario})

