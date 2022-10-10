from django.contrib import admin
from .models import clientes, servicios, solicitud, cobros
# Register your models here.
admin.site.register(clientes)
admin.site.register(servicios)
admin.site.register(solicitud)
admin.site.register(cobros)
