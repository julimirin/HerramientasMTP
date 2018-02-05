from django import forms

from .models import Solicitud

class PostSolicitud(forms.ModelForm):

    class Meta:
        model = Solicitud