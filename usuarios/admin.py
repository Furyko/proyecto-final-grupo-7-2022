from django.contrib import admin
from eventos.forms import EventoForm
from eventos.models import Evento

from usuarios.forms import UsuarioRegistroForm
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import Usuario

#admin.site.register(Usuario)
admin.site.register(Evento)
# Register your models here.


@admin.register(Usuario)
class UserAdmin(DjangoUserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),

    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2'),
        }),
    )
    
    list_display = ['id', 'username', 'email', 'first_name', 'last_name']
    search_fields = ('email', 'first_name', 'last_name', 'username')
    ordering = ('username',)

