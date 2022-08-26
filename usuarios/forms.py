from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioRegistroForm(UserCreationForm):
    class Meta:
        model=Usuario
        fields=["first_name","last_name","username","email","telefono","dni","direccion","provincia","localidad","edad","sexo","nacimiento","password1","password2",]