
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Usuario

def inicio(request):
    template = loader.get_template("../templates/master.html")
    return HttpResponse(template.render())

# Create your views here.
def saludar(request):
    template = loader.get_template("saludar.html")
    return HttpResponse(template.render())

def usuarios(request):
    template = loader.get_template("usuarios.html")
    usuarios = Usuario.objects.all().values()
    context ={
        "usuario_html": usuarios
    }
    return HttpResponse(template.render(context, request))
    