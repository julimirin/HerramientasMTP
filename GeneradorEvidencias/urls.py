from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.form_generador_evidencias, name='form_generador_evidencias'),
    url(r'^generacion/new/$', views.generacion_evidencias, name='generacion_evidencias'),
]