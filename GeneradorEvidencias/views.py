from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente

def index(request):
    return HttpResponse("GENERADOR DE EVIDENCIAS")

def form_generador_evidencias(request):
    clientes = Cliente.objects.filter(cliente="REPSOL")
    return render(request, 'GeneradorEvidencias/form_generador_evidencias.html', {'clientes': clientes})