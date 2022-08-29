from re import template
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from contacto.models import Contacto
from contacto.views import Contactos
from . import views
from django.views.generic.base import TemplateView
#from django.urls import path, reverse_lazy
from django.urls import include

from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name= "home"),
    path('iniciar-sesion/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('cerrar-sesion/',auth_views.logout_then_login, name="logout"),
    path('eventos/', views.Eventos, name= 'eventos'),
    path('recursos/', views.Recursos, name= 'recursos'),
    #path('listar/', eventosList.as_view(), name="eventolistar"),
    #path('contactos/', views.Contactos, name='contactos'),
    #path('', include ('eventos.urls')),

    



        #includes
    path("usuarios/",include("usuarios.urls")),
    path("contactos/",include("contacto.urls")),
    #path("eventos/",include("eventos.urls")),
    ]


if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )