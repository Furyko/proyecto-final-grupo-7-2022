from django.urls import reverse
from django.views.generic import ListView, CreateView,TemplateView,UpdateView,DeleteView,RedirectView
from django.shortcuts import render

from proyecto_ONG.settings import REDIRECT

import eventos
from .forms import EventoForm

from .models import Evento



class Crear(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = "eventos/crear.html"

    def get_success_url(self, **kwargs):
        return reverse('eventos:listar')


class Listar(ListView):
    model = Evento
    template_name = "eventos/listar.html"
    context_object_name = "eventos"

class Actualizar(UpdateView):
    model = Evento
    template_name = "eventos/actualizar.html"
    form_class = EventoForm

    def get_success_url(self, **kwargs):
        return reverse('eventos:listar')

class Eliminar(DeleteView):
    model = Evento
    template_name = "eventos/eliminar.html"
    
    
    def get_success_url(self, **kwargs):
        return reverse('eventos:listar')
    


"""
 class eventosList(ListView):
    model = eventos
    template_name = 'eventos/listar.html'

 class eventosCreate(CreateView):
    model = eventos
    form_class = eventoForm

"""