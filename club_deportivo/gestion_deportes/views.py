from django.shortcuts import render
from .models import Deporte

# Create your views here.
def lista_deportes(request):
    deportes = Deporte.objects.all() # Obtiene todos los deportes de la base de datos
    return render(request, 'gestion_deportes/lista_deportes.html', {'deportes': deportes}) # Envia la lista de deportes al template