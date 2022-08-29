#from .models import Categoria,Modalidad
from django.db import models
from proyecto_ONG.settings.local import DATE_INPUT_FORMATS,TIME_INPUT_FORMATS
from usuarios.models import Usuario


class Evento(models.Model):
    nombre = models.CharField(max_length=255,null=True,blank=True,name="nombre")
    lugar = models.CharField(max_length=255, null=True,blank=True,name="lugar")
    precio = models.CharField(max_length=255,null=True,blank=True,name="precio")
    #modalidad_id = models.ForeignKey(Modalidad , on_delete=models.DO_NOTHING ,name="modalidad")
    #categoria_id = models.ForeignKey(Categoria , on_delete=models.DO_NOTHING ,name="categoria")
    #participantes = models.ManyToManyField(Usuario, name="participantes")
    #slug = models.SlugField(null=True,blank=True)
    descripcion = models.TextField(max_length=255, null=True , blank=True, name="descripcion")
    localidad = models.CharField(max_length=60, null=True , blank=True, name="localidad")
    provincia = models.CharField(max_length=60, null=True , blank=True, name="provincia")
    #fecha = models.DateField(DATE_INPUT_FORMATS, null=True , blank=True,name="fecha")
    #horario = models.TimeField(TIME_INPUT_FORMATS,null=True, blank=True,name="horario")

    def __str__(self):
        return self.nombre

"""
class Modalidad(models.Model):
    nombre = models.CharField(max_length=50,null=True,blank=True,)


"""
class Categoria(models.Model):
    nombre = models.CharField(max_length=50,null=True,blank=True,)
