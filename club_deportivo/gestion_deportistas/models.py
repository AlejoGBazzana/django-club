from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Deportista(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    edad = models.PositiveIntegerField(null=False, blank=False)

    class Meta:
        ordering = ['nombre', 'edad']

    def __str__(self):
        return self.nombre

    def clean(self):
        if self.edad < 0:
            raise ValidationError('La edad no puede ser negativa.')
    
    