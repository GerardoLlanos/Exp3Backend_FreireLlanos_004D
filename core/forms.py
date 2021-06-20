from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Marca, DatosZapatilla            


class AportesForm(forms.ModelForm):
    nombre = forms.CharField(label='Nombre de zapatilla',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))   
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), label='Marca',widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    valor = forms.IntegerField(label='Valor de zapatilla', widget=forms.NumberInput(
        attrs={
            'class':'form-control'
        }
    ))
    fecha = forms.CharField(label='Fecha de lanzamiento',max_length=10, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))   
    imagen = forms.ImageField(label='Imagen', widget=forms.FileInput(
        attrs={
            'class':'form-control' 
        }
    ))

    class Meta: 
        model = DatosZapatilla
        fields = ['nombre', 'marca', 'valor', 'fecha', 'imagen']
    
     