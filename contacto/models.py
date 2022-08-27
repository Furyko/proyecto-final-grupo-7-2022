from django.db import models


class Contacto(models.Model):
    nombre = models.CharField(max_length=255, null=True , blank=True, name="nombreyapellido")
    email = models.EmailField(max_length=255, null=True , blank=True, name="email")
    asunto = models.CharField(max_length=100,null=True , blank=True, name="asunto")
    mensaje = models.TextField(max_length=255, null=True , blank=True, name="mensaje")

    def __str__(self):

        return self.nombre

