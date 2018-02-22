from django.db import models
from smart_selects.db_fields import ChainedForeignKey, \
    ChainedManyToManyField, GroupedForeignKey
import os
from .validators import validate_file_extension


class Cliente(models.Model):
    cliente = models.CharField(max_length=50, primary_key= True)
    def __str__(self):
        return self.cliente

class Plantilla(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    plantilla = models.FileField(upload_to='GeneradorEvidencias/plantillas/')
    def __str__(self):
        return os.path.basename(self.plantilla.name)

class Entorno(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    entorno = models.CharField(max_length=50)
    class Meta:
        unique_together = (('cliente', 'entorno'),)
    def __str__(self):
        return self.entorno

class FasePrueba(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fase_de_prueba = models.CharField(max_length=50)
    class Meta:
        unique_together = (('cliente', 'fase_de_prueba'),)
    def __str__(self):
        return self.fase_de_prueba

class Solicitud(models.Model):
    codigo_proyecto = models.CharField(max_length=50)
    nombre_proyecto = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    entorno = ChainedForeignKey(
        Entorno,
        chained_field="cliente",
        chained_model_field="cliente",
        show_all=False,
        auto_choose=True,
        sort=True)
    fase_de_prueba = ChainedForeignKey(
        FasePrueba,
        chained_field="cliente",
        chained_model_field="cliente",
        show_all=False,
        auto_choose=True,
        sort=True)
    archivo = models.FileField(upload_to='planes_de_prueba', validators=[validate_file_extension])
    def __str__(self):
        return self.codigo_proyecto


class CasoPrueba(models.Model):
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    codigo_caso = models.CharField(max_length=6)
    nombre_caso = models.CharField(max_length=50)
    descripcion_caso = models.CharField(max_length=500)
    def __str__(self):
        return self.codigo_caso

class PasoPrueba(models.Model):
    codigo_caso = models.ForeignKey(CasoPrueba, on_delete=models.CASCADE)
    numero_paso = models.CharField(max_length=10)
    descripcion_paso = models.CharField(max_length=500)
    resultado_paso = models.CharField(max_length=500, null=True)
    class Meta:
        unique_together = (('codigo_caso', 'numero_paso'),)
    def __str__(self):
        return self.numero_paso









