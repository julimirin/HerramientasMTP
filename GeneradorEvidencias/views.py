from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Cliente, Solicitud
from .forms import FormularioSolicitud
from django.urls import reverse

def index(request):
    return HttpResponse("GENERADOR DE EVIDENCIAS")


def form_generador_evidencias(request):
    form = FormularioSolicitud()
    return render(request, 'GeneradorEvidencias/post_solicitud.html', {'form': form})



