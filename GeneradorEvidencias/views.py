from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("GENERADOR DE EVIDENCIAS")

def form_generador_evidencias(request):
    return render(request, 'GeneradorEvidencias/form_generador_evidencias.html', {})