from django.shortcuts import render
from usuarios.models import Usuario
#from eventos.models import Evento
from django.views.generic import TemplateView


def inicio(request):
    template_name='inicio.html'
    ctx={}
    return render(request, template_name, ctx)

class ViewEventos(TemplateView):
    template_name = "eventos.html"


"""""
def Eventos(request):
    template_name = "eventos.html"

    eventos = Evento.objects.all()

    ctx = {
        'eventos': eventos
    }
    return render(request, template_name,ctx)
"""
def Recursos(request):
    template_name = "recursos.html"
    return render(request, template_name, {})
