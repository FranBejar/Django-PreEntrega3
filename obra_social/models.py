from django.db import models

# Create your models here.
class Hospital(models.Model):
    nombre=models.CharField(max_length=40)
    direccion=models.CharField(max_length=100)
    telefono=models.CharField(max_length=20)

class Afiliado(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    dni=models.CharField(max_length=10)
    telefono=models.CharField(max_length=20, blank=True)
    email=models.EmailField(max_length=32)
    fecha_de_nacimiento=models.DateField()
    direccion=models.CharField(max_length=50)
    plan=models.IntegerField()

class Especialista(models.Model):
    nombre=models.CharField(max_length=100)
    apellido=models.CharField(max_length=100)
    especialidad=models.CharField(max_length=100)
    matricula=models.IntegerField()

class Autorizacion(models.Model):
    dni_afiliado=models.CharField(max_length=10)
    plan=models.IntegerField()
    hospital=models.CharField(max_length=40)
    especialista=models.CharField(max_length=200)
    intervencion=models.CharField(max_length=100)
    observaciones=models.TextField(blank=True)
    fecha_solicitud=models.DateTimeField(auto_now_add=True)
    solicitud_aprobada=models.BooleanField(default=False)