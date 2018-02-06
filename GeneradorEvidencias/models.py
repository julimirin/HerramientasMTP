from django.db import models


class Cliente(models.Model):
    cliente = models.CharField(max_length=200)
    def __str__(self):
        return self.cliente

class Plantilla(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    plantilla = models.FileField(upload_to='GeneradorEvidencias/plantillas/')
    def __str__(self):
        return self.plantilla

class Entorno(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    entorno = models.CharField(max_length=200)
    def __str__(self):
        return self.entorno

class FasePrueba(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fase_de_prueba = models.CharField(max_length=200)
    def __str__(self):
        return self.fase_de_prueba

class Solicitud(models.Model):
    codigo_proyecto = models.CharField(max_length=200)
    nombre_proyecto = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    plantilla = models.ForeignKey(Plantilla, on_delete=models.CASCADE)
    plan_de_pruebas = models.FileField(upload_to='GeneradorEvidencias/planes_de_prueba/')
    entorno = models.ForeignKey(Entorno, on_delete=models.CASCADE)
    fase_de_prueba = models.ForeignKey(FasePrueba, on_delete=models.CASCADE)
    def __str__(self):
        return self.solicitud




