from django.urls import reverse
from django.views.generic import ListView, CreateView,TemplateView,UpdateView,DeleteView,DetailView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import SuperUserRequiredMixin
from proyecto_ONG.settings import REDIRECT

from .forms import EventoForm
from django.core.exceptions import PermissionDenied
from .models import Evento



class Crear(LoginRequiredMixin,CreateView):
    model = Evento
    form_class = EventoForm
    template_name = "eventos/crear.html"

    

    def get_success_url(self, **kwargs):
        return reverse('eventos:listar')


class Listar(ListView):
    model = Evento
    template_name = "eventos/listar.html"
    context_object_name = "eventos"
    paginate_by:5

    def get_queryset(self):
        return Evento.objects.all().order_by("id")

class Actualizar(LoginRequiredMixin,UpdateView):
    model = Evento
    template_name = "eventos/actualizar.html"
    form_class = EventoForm

    def get_success_url(self, **kwargs):
        return reverse('eventos:listar')

class Eliminar(LoginRequiredMixin,DeleteView):
    model = Evento
    template_name = "eventos/eliminar.html"
    
    
    def get_success_url(self, **kwargs):
        return reverse('eventos:listar')
    
class Detalles(LoginRequiredMixin,DetailView):
    model = Evento
    template_name = "eventos/detalles.html"
    

"""
 class eventosList(ListView):
    model = eventos
    template_name = 'eventos/listar.html'

 class eventosCreate(CreateView):
    model = eventos
    form_class = eventoForm

"""