from django.shortcuts import render
from .models import Deportista

# Create your views here.
def lista_deportistas(request):
    deportistas = Deportista.objects.all() # Obtiene todos los deportistas desde la base de datos
    return render(request, 'gestion_deportistas/lista_deportistas.html', {'deportistas': deportistas}) # Renderiza la plantilla con la lista de deportistas
