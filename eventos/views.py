from django.shortcuts import render
from datetime import datetime
from django.views import generic
from .utils import Calendar
from .models import Categoria


def Inicio(request):
    template_name = "inicio.html"
    return render(request, template_name, {})

def Informacion(request):
    template_name = "eventos_info.html"
    return render(request, template_name, {})

class EventosView(generic.ListView):
    template_name = 'eventos.html'

    def get(self, request):
        current_year = datetime.today().year
        current_month = datetime.today().month
        calendar = Calendar(current_year, current_month).formatmonth(withyear=True)
        categorias = Categoria.objects.all()
        return render(request, self.template_name, {
            "calendar": calendar,
            "categorias": categorias
            })

    def post(self, request):
        try: 
            calendar = Calendar(2022, int(request.POST['mes']), request.POST['categoria']).formatmonth(withyear=True)
        except:
            calendar = Calendar(2022, int(request.POST['mes'])).formatmonth(withyear=True)
        categorias = Categoria.objects.all()
        return render(request, self.template_name, {
            "calendar": calendar,
            "categorias": categorias
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
