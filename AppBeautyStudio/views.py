from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


from .models import Especialista, Servicio, Cliente, Cita
from .forms import EspecialistaFormulario, ServicioFormulario, ClienteFormulario, CitaFormulario

class EspecialistaList(ListView):

    model = Especialista
    template_name = 'AppBeautyStudio/especialistas-list.html'

class EspecialistaDetail(DetailView):

    model = Especialista
    template_name = 'AppBeautyStudio/especialistas-detalle.html'

class EspecialistaCreacion(CreateView):

    model = Especialista
    template_name = 'AppBeautyStudio/especialistas-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'apellidos', 'profesion']

class EspecialistaUpdate(UpdateView):

    model = Especialista
    template_name = 'AppBeautyStudio/especialistas-nuevo.html'
    success_url = reverse_lazy('inicio')
    fields = ['nombre', 'apellidos', 'profesion']

class EspecialistaDelete(DeleteView):

    model = Especialista
    template_name = 'AppBeautyStudio/especialistas-eliminar.html'
    success_url = reverse_lazy('inicio')

#from AppBeautyStudio.models import Especialistas

# Create your views here.
def inicio(request):
    return render(request,'AppBeautyStudio/Inicio.html')

def especialistas(request):
    #return render(request,'AppBeautyStudio/Especialistas.html')
    mis_especialistas = Especialista.objects.all()

    if request.method == 'POST':
        mi_formulario = EspecialistaFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            especialista = Especialista(nombre=informacion['nombre'], apellidos=informacion['apellidos'], profesion=informacion['profesion'])
            especialista.save()

            nuevo_formulario = EspecialistaFormulario()
            
            nuevo_especialista = {'nombre':informacion['nombre'], 'apellidos':informacion['apellidos'], 'profesion':informacion['profesion']}
            return render(request, 'AppBeautyStudio/Especialistas.html',{'formulario_especialistas':nuevo_formulario, 
            'nuevo_especialista':nuevo_especialista,
            'mis_especialistas':mis_especialistas})

    else: 
        mi_formulario = EspecialistaFormulario()

    return render(request, 'AppBeautyStudio/Especialistas.html', {'formulario_especialistas':mi_formulario, 'mis_especialistas':mis_especialistas})

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

def busqueda_especialista(request):
    return render(request,'AppBeautyStudio/busqueda-especialista.html')

def buscar(request):
    
    if request.GET['apellidos']:
        mi_especialista = request.GET['apellidos']
        resultado = Especialista.objects.filter(apellidos__icontains = mi_especialista)

        return render(request, 'AppBeautyStudio/especialistas.html', {'especialistas': resultado, 'especialista': mi_especialista})
    
    else:
        respuesta = 'No se encontró este especialista'
    return HttpResponse(respuesta)

def leer_servicios(request):
    servicios = Servicio.objects.all() #trae todos los servicios
    contexto = {'servicios': servicios}
    return render(request, 'AppBeautyStudio/leer-servicios.html', contexto)

def eliminar_servicio(request, servicio_id):
    servicio= Servicio.objects.get(id=servicio_id)
    servicio.delete()

    #vuelvo al menu
    servicios = Servicio.objects.all() #trae todos los servicios

    contexto= {'servicios':servicios}

    return render(request, 'AppBeautyStudio/leer-servicios.html', contexto)

def editar_servicio(request, servicio_id):
    servicio= Servicio.objects.get(id=servicio_id)

    #si es metodo POST hago lo mismo que el agregar

    if request.method =='POST':

        mi_formulario =ServicioFormulario(request.POST)  #aqui me llega toda la info del html

        print(mi_formulario)

        if mi_formulario.is_valid: #si paso la validacion de Django

            informacion = mi_formulario.cleaned_data
            servicio.servicio = informacion['servicio']
            servicio.precio = informacion['precio']

            servicio.save()

            servicios = Servicio.objects.all() 
            contexto = {'servicios': servicios}

            return render(request, 'AppBeautyStudio/leer-servicios.html', contexto)
    
    else:
        mi_formulario = ServicioFormulario(initial={'servicio':servicio.servicio, 'precio':servicio.precio})

        servicios = Servicio.objects.all()
        contexto = {'mi_formulario':mi_formulario, 'servicio_id':servicio_id}

        return render(request, 'AppBeautyStudio/editar-servicios.html', contexto)
    
def login_request(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                contexto = {'mensaje': f'Bienvenid@ {usuario}'}
                return render(request, 'AppBeautyStudio/especialistas.html', contexto)
            else:
                contexto = {'mensaje': f'El usuario no existe', 'form':form}
                return render(request, 'AppBeautyStudio/login.html', contexto)
        else:
                contexto = {'mensaje': f'datos incorrectos', 'form':form}
                return render(request, 'AppBeautyStudio/login.html', contexto)
    contexto = {'form':form}
    return render(request, 'AppBeautyStudio/login.html', contexto)
       



