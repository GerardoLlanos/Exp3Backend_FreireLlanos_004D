from django.db import models

# Create your models here.

class Marca(models.Model):
    idMarca = models.IntegerField(primary_key=True, verbose_name='id de Marca')
    nombreMarca = models.CharField(max_length= 100, verbose_name='nombre de Marca')

    def __str__(self):
        return self.nombreMarca

class DatosZapatilla(models.Model):
    nombre = models.CharField(primary_key=True, max_length= 100, verbose_name='Nombre de Zapatilla')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    valor = models.IntegerField(verbose_name='Valor')
    fecha = models.DateField(verbose_name='Fecha')
    imagen = models.ImageField(upload_to='zapatillas')

    def __str__(self):
        return self.nombre