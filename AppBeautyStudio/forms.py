from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class EspecialistaFormulario(forms.Form):
    nombre = forms.CharField()
    apellidos = forms.CharField()
    profesion = forms.CharField()

class ServicioFormulario(forms.Form):
    servicio = forms.CharField()
    precio = forms.IntegerField()

class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellidos = forms.CharField()
    telefono = forms.IntegerField()
    email = forms.EmailField()

class CitaFormulario(forms.Form):
    apellidos_especialista = forms.CharField()
    fecha_cita = forms.DateField()
    reservado = forms.BooleanField(required=False, initial=True)

class MyUserCreationForm(UserCreationForm):
    
    username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repite la contraseña', widget=forms.PasswordInput)

    class Meta():

        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}

class UserEditForm(UserCreationForm):
    username = forms.CharField(label='Nombre de Usuario')
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta():
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {k: '' for k in fields}

