from django.urls import path

from . import views

urlpatterns = [
    path('', views.form_generador_evidencias, name='form_generador_evidencias'),

]