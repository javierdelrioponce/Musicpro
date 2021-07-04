from django.db import models
from django.utils import timezone

# Create your models here.

class Productos(models.Model):
    Id = models.CharField(max_length=10, primary_key=True)
    Autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    Tipo = models.CharField(max_length=50)
    Descripcion = models.TextField()
    

    def __str__(self):
        return self.nombre