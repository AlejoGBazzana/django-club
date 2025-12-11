from django.contrib import admin
from .models import Socio

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'fecha_inscripcion')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('fecha_inscripcion',)
    ordering = ('apellido', 'nombre')