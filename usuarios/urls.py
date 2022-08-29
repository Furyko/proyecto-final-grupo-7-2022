from django.urls import path

from usuarios.models import Usuario

from .import views
#from proyecto_ONG import usuarios

app_name="usuarios"

urlpatterns = [
    path('registro/', views.Registro.as_view(), name='registro'),
]