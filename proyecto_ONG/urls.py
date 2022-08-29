from re import template
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin
from django.views.static import serve
from django.contrib.auth import views as auth_views
from contacto.models import Contacto
from contacto.views import Contactos
from django.views.generic.base import TemplateView
#from django.urls import path, reverse_lazy



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('eventos.urls')),
       
]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )
    path('', views.inicio, name= "home"),
    path('iniciar-sesion/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('cerrar-sesion/',auth_views.logout_then_login, name="logout"),
    path('eventos/', views.Eventos, name= 'eventos'),
    path('recursos/', views.Recursos, name= 'recursos'),
    #path('listar/', eventosList.as_view(), name="eventolistar"),
    #path('contactos/', views.Contactos, name='contactos'),

        #includes
    path("usuarios/",include("usuarios.urls")),
    path("contactos/",include("contacto.urls")),
    #path("eventos/",include("eventos.urls")),
    
