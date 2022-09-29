from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context
from django.template.loader import get_template

# vistas para la aplicacion solicitud_servicios

def inicio(request):
    
    return render(request,"inicio.html")

def nuevo_servicio(request):
    pass