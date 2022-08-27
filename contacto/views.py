
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
#from .forms import UserCreationForm, UsuarioRegistroForm
#from .models import Usuario
from .forms import ContactoForm

"""""

class ContactoCreateView(CreateView):
    form_class = ContactoForm
    template_name = "contactos/contactos.html"
   
"""""

def Contactos(request):

    data = {
        'form': ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
            
    
    template_name= "contactos/contactos.html"
    print(template_name)
    return render(request, template_name, data)

