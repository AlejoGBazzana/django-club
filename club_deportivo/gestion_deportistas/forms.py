from django import forms
from .models import Deportista

class DeportistaForm(forms.ModelForm):
    class Meta:
        model = Deportista
        fields = ['nombre', 'edad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Edad'}),
        }
