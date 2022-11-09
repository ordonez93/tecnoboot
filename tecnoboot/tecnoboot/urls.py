from django.contrib import admin
from django.urls import path
from Aplicaciones.solicitud_servicios.views import *


urlpatterns = [
    path('',inicio),
    path('admin/', admin.site.urls),
    path('solicitarServicio/',solicitarServicio),
    path('acercade/',acercade),
    path('pag_servicios/',pag_servicios),
      
]
