from ast import If
from turtle import textinput
from xml.dom.minidom import Attr
from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"g-col-6 g-col-md-4"}))
    #lugar = forms.CharField(widget=forms.TextInput(attrs={"class":"g-col-6 g-col-md-4"}))
    #precio = forms.CharField(widget=forms.TextInput(attrs={"class":"g-col-6 g-col-md-4"}))
    class Meta:
        model = Evento
        fields = ["nombre","lugar","precio","descripcion","provincia","localidad"]
        


