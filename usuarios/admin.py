from django.contrib import admin

from usuarios.forms import UsuarioRegistroForm

from .models import Usuario

admin.site.register(Usuario)
#admin.site.register(UsuarioRegistroForm)
# Register your models here.
