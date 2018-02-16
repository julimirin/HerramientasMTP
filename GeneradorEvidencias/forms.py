from django import forms

from .models import Solicitud, Cliente, Entorno, FasePrueba


class FormularioSolicitud(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = [
            "codigo_proyecto",
            "nombre_proyecto",
            "cliente",
            "entorno",
            "fase_de_prueba",
            "plan_de_pruebas"
        ]

    def __init__(self, *args, **kwargs):
        super(FormularioSolicitud, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})







