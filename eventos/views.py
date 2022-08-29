from django.urls import reverse
from django.views.generic import ListView, CreateView,TemplateView
from django.shortcuts import render
from .forms import EventoForm

from .models import Evento



class Crear(CreateView):
    model = Evento
    form_class = EventoForm
    template_name = "eventos/crear.html"

    def get_success_url(self, **kwargs):
        return reverse('eventos')


class Listar(ListView):
    model = Evento
    template_name = "eventos/listar.html"
    context_object_name = "eventos"




"""
 class eventosList(ListView):
    model = eventos
    template_name = 'eventos/listar.html'

 class eventosCreate(CreateView):
    model = eventos
    form_class = eventoForm

"""