from django import forms

from usuarios.models import Usuario
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        
        #fields =["nombre","email"]
        fields = "__all__"
