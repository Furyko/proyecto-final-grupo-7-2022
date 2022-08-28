from django.shortcuts import render
from datetime import datetime
from .utils import Calendar


def Inicio(request):
    template_name = "inicio.html"
    return render(request, template_name, {})

def Informacion(request):
    template_name = "eventos_info.html"
    return render(request, template_name, {})

def Eventos(request):
    current_year = datetime.today().year
    current_month = datetime.today().month
    calendar = Calendar(current_year, current_month).formatmonth(withyear=True)
    template_name = "eventos.html"
    return render(request, template_name, {
        "calendar": calendar
        })

def Recursos(request):
    template_name = "recursos.html"
    return render(request, template_name, {})

def Contactos(request):
    template_name= "contactos.html"
    return render(request, template_name, {})

def Login(request):
    template_name= "login.html"
    return render(request, template_name, {})

def Register(request):
    template_name= "register.html"
    return render(request, template_name, {})
