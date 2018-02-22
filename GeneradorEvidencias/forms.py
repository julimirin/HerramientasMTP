from django import forms
from .models import Solicitud, FasePrueba

class GenerarForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = [
            "codigo_proyecto",
            "nombre_proyecto",
            "cliente",
            "entorno",
            "fase_de_prueba",
            "archivo",
        ]


    def __init__(self, *args, **kwargs):
        super(GenerarForm, self).__init__(*args, **kwargs)
        for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control'})




