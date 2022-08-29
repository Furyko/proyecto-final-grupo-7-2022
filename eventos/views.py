from django.urls import reverse
from django.views.generic import ListView, CreateView,TemplateView,UpdateView,DeleteView,DetailView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import SuperUserRequiredMixin
from proyecto_ONG.settings.local import REDIRECT

from .forms import EventoForm
from django.core.exceptions import PermissionDenied
from .models import Evento

from .models import Categoria

from django.views import generic
from .utils import Calendar
from datetime import datetime


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

"""
 class eventosList(ListView):
    model = eventos
    template_name = 'eventos/listar.html'

 class eventosCreate(CreateView):
    model = eventos
    form_class = eventoForm

"""