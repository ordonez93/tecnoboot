from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template, context
from django.template.loader import get_template
from .models import clientes, servicios, solicitud
from django.contrib import messages
import datetime
# vistas para la aplicacion solicitud_servicios

def inicio(request):
    listaServicios = servicios.objects.all()
    fecha_now = datetime.datetime.now()
    return render(request,"inicio.html",{"servicios":listaServicios,"fecha": fecha_now.year})

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
        messages.success(request, 'Solicitud enviada con exito!')
        return redirect(to=inicio)
    else:
        messages.error(request, 'la solicitud no se pudo enviar')
        return redirect(to=inicio)


def acercade(request):
    return render(request,"aboutus.html")

def pag_servicios(request):
    listaServicios = servicios.objects.all()
    return render(request,"servicios.html",{"servicios":listaServicios})