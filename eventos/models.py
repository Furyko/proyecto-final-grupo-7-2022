from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    email = models.CharField(max_length=320)
    telefono = models.IntegerField(blank=True, null=True)
    localidad = models.CharField(max_length=60)
    provincia = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField(blank=True, null=True)

class Modalidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    nombre = models.CharField(max_length=64)
    detalle = models.TextField(max_length=500)
    calle = models.CharField(max_length=60)
    numero_calle = models.IntegerField()
    localidad = models.CharField(max_length=60)
    provincia = models.CharField(max_length=60)
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    horario = models.TimeField(auto_now=False, auto_now_add=False)
    costo = models.CharField(max_length=20)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    link = models.CharField(max_length=1000)
    modalidad_id = models.ForeignKey(Modalidad, on_delete=models.DO_NOTHING)
    categoria_id = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    participantes = models.ManyToManyField(Usuario)

#Archivos media para descargar   
    
class Document(models.Model):
    title = models.CharField(max_length = 50)
    uploadedFile = models.FileField(upload_to = 'media')
    dateTimeOfUpload = models.DateTimeField(auto_now = True)
    descripcion =models.CharField(max_length = 100,blank=True, null=True)
    
    
    def __str__(self):

        return self.title
