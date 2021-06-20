from django.shortcuts import render, redirect
from .models import DatosZapatilla
from .forms import AportesForm

# Create your views here.

def home(request):

    return render(request, 'home.html')

def Ver(request):
    verzapatillas = DatosZapatilla.objects.all()

    return render(request, 'core/ver.html', context={'verzapatillas':verzapatillas})


def form_aportes(request):
    if request.method == 'POST': 
        aportes_form = AportesForm(request.POST)
        if aportes_form.is_valid():
            aportes_form.save()        #similar al insert de un modelo relacional 
            return redirect('home')
    else: 
        aportes_form = AportesForm()
    return render(request, 'core/form_aportes.html', {'aportes_form': aportes_form})


def form_mod_zapatillas(request, id):
    zapatilla = DatosZapatilla.objects.get(nombre=id)

    datos ={
        'form': AportesForm(instance=zapatilla)
    }
    
    if request.method == 'POST': 
        formulario = AportesForm(data=request.POST, instance = zapatilla)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/form_mod_zapatillas.html', datos)