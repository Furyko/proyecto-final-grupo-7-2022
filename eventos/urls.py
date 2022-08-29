from django.urls import path
from .import views

app_name="eventos"


urlpatterns = [
    path('crear/', views.Crear.as_view(), name='crear'),
    path('listar/', views.Listar.as_view(), name='listar'),
    path('actualizar/<int:pk>/', views.Actualizar.as_view(), name='actualizar'),
    path('eliminar/<int:pk>/', views.Eliminar.as_view(), name='eliminar'),
]
