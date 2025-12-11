from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Deporte
from .forms import DeporteForm

# Create your views here.
def lista_deportes(request):
    deportes = Deporte.objects.all() # Obtiene todos los deportes de la base de datos
    return render(request, 'gestion_deportes/lista_deportes.html', {'deportes': deportes}) # Envia la lista de deportes al template

def detalle_deporte(request, pk):
    deporte = get_object_or_404(Deporte, pk=pk)
    deportistas = deporte.deportistas.all()
    return render(request, 'gestion_deportes/detalle_deporte.html', {'deporte': deporte, 'deportistas': deportistas})

@staff_member_required
def crear_deporte(request):
    form = DeporteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestion_deportes:lista_deportes')
    return render(request, 'gestion_deportes/form_deporte.html', {'form': form, 'titulo': 'Crear Deporte'})

@staff_member_required
def editar_deporte(request, pk):
    obj = get_object_or_404(Deporte, pk=pk)
    form = DeporteForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('gestion_deportes:lista_deportes')
    return render(request, 'gestion_deportes/form_deporte.html', {'form': form, 'titulo': 'Editar Deporte', 'obj': obj})

@staff_member_required
def eliminar_deporte(request, pk):
    obj = get_object_or_404(Deporte, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('gestion_deportes:lista_deportes')
    return render(request, 'gestion_deportes/confirmar_eliminar.html', {'obj': obj})