from django import forms
from django.forms import ModelForm
from.models import Document

#crear un recursos form

class RecursosForm(ModelForm):
    class Meta:
        model = Document
        fields = "__all__"