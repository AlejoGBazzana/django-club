from django.db import models

# Creamos el modelo de Socio

class Socio(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['apellido', 'nombre']
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"