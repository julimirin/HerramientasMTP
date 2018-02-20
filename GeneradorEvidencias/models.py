from django.db import models
from smart_selects.db_fields import ChainedForeignKey, \
    ChainedManyToManyField, GroupedForeignKey
import os
from .validators import validate_file_extension


class Cliente(models.Model):
    cliente = models.CharField(max_length=50)
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
    def __str__(self):
        return self.entorno

class FasePrueba(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fase_de_prueba = models.CharField(max_length=50)
    def __str__(self):
        return self.fase_de_prueba

#class PlanPrueba(models.Model):
#    codigo_proyecto = models.CharField(max_length=50)
#    nombre_proyecto = models.CharField(max_length=50)
#    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
#    archivo = models.FileField(upload_to='planes_de_prueba', validators=[validate_file_extension])

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






