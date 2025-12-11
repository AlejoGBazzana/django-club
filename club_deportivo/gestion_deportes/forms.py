from django import forms
from .models import Deporte

class DeporteForm(forms.ModelForm):
    class Meta:
        model = Deporte
        fields = ['nombre', 'deportistas']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del deporte'}),
            'deportistas': forms.CheckboxSelectMultiple(),
        }
