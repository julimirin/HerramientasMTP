from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Cliente, Solicitud
from .forms import FormularioSolicitud
from django.urls import reverse
import time


def index(request):

    return HttpResponse("GENERADOR DE EVIDENCIAS")


def generacion_evidencias(request):

    return HttpResponse("GENERANDOSE EVIDENCIAS")


def form_generador_evidencias(request):

    if request.method == "POST":
        form = FormularioSolicitud(request.POST, request.FILES)
        print("Validar formulario")
        file = request.FILES['plan_de_pruebas']
        print(file)
        if form.is_valid():
            print("Formulario sin errores")
            solicitud = form.save()

            #solicitud.plantilla()
            #solicitud.plan_de_pruebas()
            solicitud.save()
            return redirect('generacion_evidencias')
        else:
            for error in form.errors:
                print("Error en campo", error)
    else:
        form = FormularioSolicitud()
        print("traza")

    print ("Escribimos el request", request)
    return render(request, 'GeneradorEvidencias/post_solicitud.html', {'form': form})




