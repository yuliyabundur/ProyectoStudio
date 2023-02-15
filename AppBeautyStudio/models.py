from django.db import models

# Create your models here.
class Especialistas(models.Model):

    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    profesion = models.CharField(max_length=30)

class Clientes(models.Model):

    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    telefono = models.IntegerField()
    email = models.EmailField()

class Servicios(models.Model):

    servicio = models.CharField(max_length=50)
    precio = models.IntegerField()

class Citas(models.Model):

    apellidos_especialista = models.CharField(max_length=40)
    fecha_cita = models.DateField()
    reservado = models.BooleanField()
    
   