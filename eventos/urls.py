from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = "Eventos"

urlpatterns = [

    #path("", views.uploadFile, name = "uploadFile"),

    path('inicio/', views.Inicio, name= 'inicio'),
    path('eventos_info/', views.Informacion, name= 'eventos_info'),
    path('eventos/', views.Eventos, name= 'eventos'),
    path('recursos/', views.Recursos, name= 'recursos'),
    path('contactos/', views.Contactos, name= 'contactos'),
    path('login/', views.Login, name= 'login'),
    path('register/', views.Register, name= 'register')

]

if settings.DEBUG: 
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root = settings.MEDIA_ROOT
    )