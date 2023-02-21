from django import forms

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
