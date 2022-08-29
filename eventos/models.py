from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=255,null=True,blank=True,name="nombre")
    lugar = models.CharField(max_length=255, null=True,blank=True,name="lugar")
    precio = models.CharField(max_length=255,null=True,blank=True,name="precio")

    def __str__(self):
        return self.nombre
