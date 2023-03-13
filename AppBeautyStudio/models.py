from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Especialista(models.Model):

    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre +' '+ self.apellidos

class Cliente(models.Model):

    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    telefono = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.apellidos

class Servicio(models.Model):

    servicio = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.servicio

class Cita(models.Model):

    apellidos_especialista = models.CharField(max_length=40)
    fecha_cita = models.DateField()
    reservado = models.BooleanField()

    def __str__(self):
        return self.fecha_cita
    
class Avatar(models.Model):
    #vinculo con el perfil del usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True, default='blank.jpg')

    def __str__(self):
        self.user.username
    
   