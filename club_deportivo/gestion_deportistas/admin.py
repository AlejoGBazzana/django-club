from django.contrib import admin
from .models import Deportista

# Register your models here.
@admin.register(Deportista)
class DeportistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'edad')  # Campos a mostrar en la lista del admin
    search_fields = ('nombre',)  # Campos por los que se puede buscar
    ordering = ('edad','nombre')  # Ordenamiento por defecto