from . import models
from django.shortcuts import render
import templates


def Inicio(request):
    template_name = "inicio.html"
    return render(request, template_name, {})

def Informacion(request):
    template_name = "eventos_info.html"
    return render(request, template_name, {})

def Eventos(request):
    template_name = "eventos.html"
    return render(request, template_name, {})

def Recursos(request):
    template_name = "recursos.html"
    return render(request, template_name, {})

def Contactos(request):
    template_name= "contactos.html"
    return render(request, template_name, {})

def Login(request):
    template_name= "login.html"
    return render(request, template_name, {})

def Register(request):
    template_name= "register.html"
    return render(request, template_name, {})

def uploadFile(request):
    if request.method == "POST":
        # Fetching the form data
        fileTitle = request.POST["fileTitle"]
        uploadedFile = request.FILES["uploadedFile"]

        # Saving the information in the database
        document = models.Document(
            title = fileTitle,
            uploadedFile = uploadedFile
        )
        document.save()

    documents = models.Document.objects.all()

    return render(request, "eventos/upload-file.html", context = {
        "files": documents
    })