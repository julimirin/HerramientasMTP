from django.http import HttpResponse
from django.shortcuts import render
from .models import Cliente
from .forms import PostSolicitud

def index(request):
    return HttpResponse("GENERADOR DE EVIDENCIAS")

def form_generador_evidencias(request):
    clientes = Cliente.objects.filter(cliente="VODAFONE")
    form = PostSolicitud()
    return render(request, 'GeneradorEvidencias/post_solicitud.html', {'form': form})