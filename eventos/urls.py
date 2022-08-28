from . import views
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import serve


app_name = "Eventos"

urlpatterns = [
   
    path('inicio/', views.Inicio, name= 'inicio'),
    path('eventos_info/', views.Informacion, name= 'eventos_info'),
    path('eventos/', views.Eventos, name= 'eventos'),
    path('recursos/', views.Recursos, name= 'recursos'),
    path('contactos/', views.Contactos, name= 'contactos'),
    path('login/', views.Login, name= 'login'),
    path('register/', views.Register, name= 'register'),
    path("recursos_subir/", views.uploadFile, name = "uploadFile"),    

]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )