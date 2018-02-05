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




