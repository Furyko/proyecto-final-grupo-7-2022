from django.db import models



class Usuario(models.User):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    telefono = models.IntegerField(max_length=15)
    localidad = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)
    anio_nacimiento = models.IntegerField(max_length=4)
    mes_nacimiento = models.IntegerField(max_length=2)
    dia_nacimiento = models.IntegerField(max_length=2)

class Costo(models.Model):
    precio = models.IntegerField(max_length=50)

class Modalidad(models.Model):
    nombre = models.CharField(max_length=50)

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    detalle = models.CharField(max_length=500)
    horario = models.TimeField(auto_now=False, auto_now_add=False)
    calle = models.CharField(max_length=200)
    numero_calle = models.IntegerField(max_length=10)
    localidad = models.CharField(max_length=200)
    provincia = models.CharField(max_length=200)
    anio_evento = models.IntegerField(max_length=4)
    mes_evento= models.IntegerField(max_length=2)
    dia_evento = models.IntegerField(max_length=2)
    costo_id = models.ForeignKey(Costo)
    modalidad_id = models.ForeignKey(Modalidad)
