from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, context
from django.template.loader import get_template
from .models import clientes, servicios, solicitud, cobros
# vistas para la aplicacion solicitud_servicios

def inicio(request):
    listaServicios = servicios.objects.all()
    return render(request,"inicio.html",{"servicios":listaServicios})

def solicitarServicio(request):
    if request.method == "POST":
        cliente = clientes()
        cliente.nombre = request.POST["nombre"]
        cliente.apellido = request.POST["apellido"]
        cliente.ciudad = request.POST["ciudad"]
        cliente.telefono = request.POST["telefono"]
        cliente.direccion = request.POST["direccion"]
        cliente.save()
        servicio = servicios.objects.get(id=request.POST["servicio"])
        solicitudServicio = solicitud()
        solicitudServicio.cliente = cliente
        solicitudServicio.servicio = servicio
        solicitudServicio.save()
        return HttpResponse("Solicitud enviada")
    else:
        return HttpResponse("No se pudo enviar la solicitud")

def acercade(request):
    return render(request,"aboutus.html")