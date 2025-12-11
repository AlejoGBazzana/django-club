from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Deportista
from .forms import DeportistaForm

# Create your views here.
def lista_deportistas(request):
    deportistas = Deportista.objects.all() # Obtiene todos los deportistas desde la base de datos
    return render(request, 'gestion_deportistas/lista_deportistas.html', {'deportistas': deportistas}) # Renderiza la plantilla con la lista de deportistas

def detalle_deportista(request, pk):
    deportista = get_object_or_404(Deportista, pk=pk)
    return render(request, 'gestion_deportistas/detalle_deportista.html', {'deportista': deportista})

@staff_member_required
def crear_deportista(request):
    form = DeportistaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestion_deportistas:lista_deportistas')
    return render(request, 'gestion_deportistas/form_deportista.html', {'form': form, 'titulo': 'Crear Deportista'})

@staff_member_required
def editar_deportista(request, pk):
    obj = get_object_or_404(Deportista, pk=pk)
    form = DeportistaForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('gestion_deportistas:lista_deportistas')
    return render(request, 'gestion_deportistas/form_deportista.html', {'form': form, 'titulo': 'Editar Deportista', 'obj': obj})

@staff_member_required
def eliminar_deportista(request, pk):
    obj = get_object_or_404(Deportista, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('gestion_deportistas:lista_deportistas')
    return render(request, 'gestion_deportistas/confirmar_eliminar.html', {'obj': obj})
