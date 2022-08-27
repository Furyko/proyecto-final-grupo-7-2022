from django.shortcuts import render
from usuarios.models import Usuario


def inicio(request):
    template_name='inicio.html'
    ctx={}
    return render(request, template_name, ctx)

def Eventos(request):
    template_name = "eventos.html"
    return render(request, template_name, {})

def Recursos(request):
    template_name = "recursos.html"
    return render(request, template_name, {})







    
"""
def login(request):
    print(request.POST)
    nombre_usuario = request.POST.get("usurname", None)
    contrasenia = request.POST.get("password", None)
    return render(request,'login.html', {})
"""