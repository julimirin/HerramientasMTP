from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Entorno, Cliente, FasePrueba, Plantilla, Solicitud

admin.site.register(Entorno)
admin.site.register(Cliente)
admin.site.register(FasePrueba)
admin.site.register(Plantilla)
admin.site.register(Solicitud)
