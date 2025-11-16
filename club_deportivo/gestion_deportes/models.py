from django.db import models
from django.core.exceptions import ValidationError
from gestion_deportistas.models import Deportista

# Create your models here.
class Deporte(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    deportistas = models.ManyToManyField(Deportista, related_name='deportes')
    
    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def clean(self):
        if not self.nombre:
            raise ValidationError('El nombre del deporte no puede estar vacío.')