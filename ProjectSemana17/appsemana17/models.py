from django.db import models

class Area(models.Model):
    nombre_del_area = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    dui = models.IntegerField()

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

class Venta(models.Model):
    fecha_venta = models.CharField(max_length=100)
    monto = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
