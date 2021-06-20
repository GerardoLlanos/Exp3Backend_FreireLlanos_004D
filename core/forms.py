from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Marca, DatosZapatilla            


class AportesForm(forms.ModelForm):

    class Meta: 
        model = DatosZapatilla
        fields = ['nombre', 'marca', 'valor', 'fecha']
    
        labels={
            'nombre': 'Nombre de Zapatilla: ',
            'marca': 'Marca de Zapatilla: ',
            'valor': 'Valor de Zapatilla: ', 
            'fecha': 'Fecha de Lanzamiento: ',
            'imagen': 'Imagen de Zapatilla: '

        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre', 
                    'placeholder': 'Digite nombre'
                }
            ),
            'marca': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'marca', 
                }
            ), 
            'valor': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'id': 'valor', 
                    'placeholder': 'Digite valor'
                }
            ),
            'fecha': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'fecha',
                    'placeholder': '01/01/2021'
                }
            ),
        }