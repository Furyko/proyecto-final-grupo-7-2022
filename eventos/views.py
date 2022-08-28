from django.views.generic import ListView, CreateView
from django.shortcuts import render



class eventosList(ListView):
    model = eventos
    template_name = 'eventos/listar.html'

class eventosCreate(CreateView):
    model = eventos
    form_class = eventoForm

