from django import forms
from .models import Solicitud, FasePrueba

class UploadForm(forms.ModelForm):

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
        super(UploadForm, self).__init__(*args, **kwargs)
        for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

'''
class FaseForm(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = [
            "entorno",
            "fase_de_prueba",
        ]

    def __init__(self, *args, **kwargs):
        super(FaseForm, self).__init__(*args, **kwargs)
        for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control'})



class FormularioSolicitud(forms.ModelForm):

    class Meta:
        model = Solicitud
        fields = [
        "entorno",
        "fase_de_prueba",
        "plan_de_prueba",
        ]


    def __init__(self, *args, **kwargs):
        super(FormularioSolicitud, self).__init__(*args, **kwargs)
        for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control'})

'''





