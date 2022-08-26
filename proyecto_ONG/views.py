from django.shortcuts import render
from usuarios.models import Usuario


def inicio(request):
    template_name='inicio.html'
    ctx={}
    return render(request, template_name, ctx)
"""
def login(request):
    print(request.POST)
    nombre_usuario = request.POST.get("usurname", None)
    contrasenia = request.POST.get("password", None)
    return render(request,'login.html', {})
"""