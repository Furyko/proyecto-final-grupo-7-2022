from django.db import models
from django.contrib.auth.models import AbstractUser

from proyecto_ONG.settings import DATE_INPUT_FORMATS

class Usuario(AbstractUser):
    telefono = models.CharField(max_length=255, null=True, blank=True ,name="telefono")
    edad = models.PositiveIntegerField(null=True, blank=True ,name="edad")
    provincia = models.CharField(max_length=255, null=True, blank=True, name="provincia")
    localidad = models.CharField(max_length=255, null=True, blank=True, name="localidad")
    direccion = models.CharField(max_length=255, null=True, blank=True, name="direccion")
    sexo = models.CharField(max_length=255, null=True, blank=True, name="sexo")
    dni = models.CharField(max_length=255, null=True, blank=True, name="dni")
    fecha_nacimiento = models.DateField(DATE_INPUT_FORMATS,null=True, blank=True, name="nacimiento")
    #es_administrador = models.BooleanField(default=False)
    

    def __str__(self):
        return self.first_name
