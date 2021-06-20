# Llama los métodos creados en views

from django.urls import path #libreria para llamar a los métodos
from .views import home #va al archivo views y busca el método

urlpatterns =[  #Parámetro para crear un path

    path('', home, name="home"), #creamos el path para que sea la primera página
]