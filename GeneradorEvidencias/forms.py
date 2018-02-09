from django import forms

from .models import Solicitud, Cliente, Entorno, FasePrueba


class PostSolicitud(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = ('codigo_proyecto','nombre_proyecto','cliente','entorno','fase_de_prueba','plan_de_pruebas')




