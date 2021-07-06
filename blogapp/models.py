from django.db import models
from django.utils import timezone

# Create your models here.

class Producto(models.Model):    
    serie = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    codigo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=30)    
    created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha creacion')
    updated = models.DateTimeField(auto_now=True,verbose_name='Fecha Modificacion')
    valor = models.IntegerField()


    def __str__(self):
        return self.nombre