from re import template
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from contacto.models import Contacto
from contacto.views import Contactos
#from eventos.views import ViewEventos
from . import views
from django.views.generic.base import TemplateView
#from django.urls import path, reverse_lazy
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name= "home"),
    path('iniciar-sesion/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('cerrar-sesion/',auth_views.logout_then_login, name="logout"),
    path('eventos/', views.ViewEventos.as_view(template_name="eventos.html"), name= 'eventos'),
    path('recursos/', views.Recursos, name= 'recursos'),
    #path('listar/', eventosList.as_view(), name="eventolistar"),
    #path('contactos/', views.Contactos, name='contactos'),

    



        #includes
    path("usuarios/",include("usuarios.urls")),
    path("contactos/",include("contacto.urls")),
    path("eventos/",include("eventos.urls")),
    ]