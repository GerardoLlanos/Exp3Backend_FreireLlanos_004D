from django.shortcuts import render
# from .models import Vehiculo
# from .forms import VehiculoForm

def home(request):

    return render(request, 'home.html')
 

# Create your views here.
# def home(request):
#     nombre = 'Claudia Andrea'
#     lista = ["Cazuela", "Porotos", "Pizza"]
#     vehiculos=Vehiculo.objects.all()    #es similar al comando select de consultas 
#     return render(request, 'home.html', context={'nombre_usuario':nombre,'comidas':lista,
#     'autos':vehiculos})

# def form_vehiculo(request):
#     if request.method == 'POST': 
#         vehiculo_form = VehiculoForm(request.POST)
#         if vehiculo_form.is_valid():
#             vehiculo_form.save()        #similar al insert de un modelo relacional 
#             return redirect('home')
#     else: 
#         vehiculo_form = VehiculoForm()
#     return render(request, 'core/form_crearvehiculo.html', {'vehiculo_form': vehiculo_form})




 