from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from .models import Socio
from .forms import SocioForm

def lista_socios(request):
    socios = Socio.objects.all()
    return render(request, 'gestion_socios/lista_socios.html', {'socios': socios})

def detalle_socio(request, pk):
    socio = get_object_or_404(Socio, pk=pk)
    return render(request, 'gestion_socios/detalle_socio.html', {'socio': socio})

@staff_member_required
def crear_socio(request):
    form = SocioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestion_socios:lista_socios')
    return render(request, 'gestion_socios/form_socio.html', {'form': form, 'titulo': 'Registrar Socio'})

@staff_member_required
def editar_socio(request, pk):
    obj = get_object_or_404(Socio, pk=pk)
    form = SocioForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('gestion_socios:lista_socios')
    return render(request, 'gestion_socios/form_socio.html', {'form': form, 'titulo': 'Editar Socio', 'obj': obj})

@staff_member_required
def eliminar_socio(request, pk):
    obj = get_object_or_404(Socio, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('gestion_socios:lista_socios')
    return render(request, 'gestion_socios/confirmar_eliminar.html', {'obj': obj})