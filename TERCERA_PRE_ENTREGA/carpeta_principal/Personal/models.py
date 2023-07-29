from django.db import models

# Create your models here.


class Operador(models.Model):
    nombre = models.CharField(max_length=230)
    numero_legajo = models.CharField(max_length=230)
    antiguedad: models.IntegerField(null=True)
    puesto: models.CharField(max_length=230)


class Supervisor(models.Model):
    nombre = models.CharField(max_length=230)
    area = models.CharField(max_length=230)
    antiguedad =  models.IntegerField(null=True)


class Gerente(models.Model):
    nombre=models.CharField(max_length=230)
    area = models.CharField(max_length=230)
    antiguedad = models.IntegerField(null=True)
    descripcion= models.TextField()