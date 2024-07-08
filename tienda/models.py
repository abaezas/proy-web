from django.db import models

# Create your models here.

class tipoProducto(models.Model):

    nombre      = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    nombre      = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio      = models.IntegerField()
    stock       = models.IntegerField()
    imagen      = models.ImageField(upload_to='productos', null=True)
    tipo        = models.ForeignKey(tipoProducto, on_delete=models.PROTECT)

    def __str__(self):
        return self.nombre