from django.urls import path

from usuarios.models import Usuario
from contacto.models import Contacto

from .import views
#from proyecto_ONG import usuarios

app_name="contacto"

urlpatterns = [
    path('contactos/',views.Contactos, name='contactos'),
]