from re import template
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView
#from django.urls import path, reverse_lazy
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name= "home"),
    path('iniciar-sesion/',auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('cerrar-sesion/',auth_views.logout_then_login, name="logout"),
    



        #includes
    path("usuarios/",include("usuarios.urls")),
    ]