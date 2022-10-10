from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context
from django.template.loader import get_template
from .models import clientes, servicios, solicitud, cobros
# vistas para la aplicacion solicitud_servicios

def inicio(request):
    listaServicios = servicios.objects.all()
    return render(request,"inicio.html",{"servicios":listaServicios})

