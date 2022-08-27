from django.shortcuts import render
from usuarios.models import Usuario


def inicio(request):
    template_name='inicio.html'
    ctx={}
    return render(request, template_name, ctx)

def Eventos(request):
    template_name = "eventos.html"
    return render(request, template_name, {})

def Recursos(request):
    template_name = "recursos.html"
    return render(request, template_name, {})
