from django.contrib import admin
from .models import Deporte

# Register your models here.
@admin.register(Deporte)
class DeporteAdmin(admin.ModelAdmin):
    list_display = ('nombre',)  # Campos a mostrar en la lista del admin
    search_fields = ('nombre',)  # Campos por los que se puede buscar
    filter_horizontal = ('deportistas',)  # Campos ManyToMany con filtro horizontal
    list_filter = ('deportistas',)  # Filtros laterales (vacío en este caso)
    fields = ['nombre', 'deportistas']  # Campos a mostrar en el formulario de edición

    def get_deportistas(self, obj):
        return ", ".join([str(deportista) for deportista in obj.deportistas.all()])