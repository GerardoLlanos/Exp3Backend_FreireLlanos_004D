from django.shortcuts import render
from .models import DatosZapatilla

# Create your views here.

def home(request):

    return render(request, 'home.html')

def Ver(request):
    verzapatillas = DatosZapatilla.objects.all()

    return render(request, 'core/ver.html', context={'verzapatillas':verzapatillas})