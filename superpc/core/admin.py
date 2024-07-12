from django.contrib import admin
from .models import Solicitud, Marca,Vehiculo


# Register your models here.

admin.site.register(Solicitud)
admin.site.register(Marca)
admin.site.register(Vehiculo)