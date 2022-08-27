from . import models
from django.shortcuts import render
import templates

def inicio(request):
    return render(request,'inicio.html',{})

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