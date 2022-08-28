from django.contrib import admin
from eventos.models import Evento

from usuarios.models import Usuario


admin.site.register(Usuario)
admin.site.register(Evento)
# Register your models here.
