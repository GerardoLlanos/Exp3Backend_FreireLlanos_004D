from django import forms
from django.forms import ModelForm,widgets 
# from .models import Vehiculo


# class VehiculoForm(ModelForm):

#     class Meta: 
#         model = Vehiculo
#         fields = ['patente', 'marca', 'modelo', 'categoria']
    
#         labels={
#             'patente': 'Patente: ',
#             'marca': 'Marca: ',
#             'modelo': 'Modelo: ', 
#             'categoria': 'Categoria: ',

#         }
#         widgets={
#             'patente': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'patente', 
#                     'name': 'patente',
#                     'placeholder': 'Digite patente'
#                 }
#             ),
#             'marca': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'marca', 
#                     'placeholder': 'Digite marca'

#                 }
#             ), 
#             'modelo': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'modelo', 
#                     'placeholder': 'Digite modelo'

#                 }
#             ),
#             'categoria': forms.Select(
#                 attrs={
#                     'class': 'form-control',
#                     'id': 'categoria'
#                 }
#             )
#         }

