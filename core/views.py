from django.shortcuts import render

# Create your views here.
# Create methods here
def home(request):
    nombre='Claudia Andrea'
    lista=["Pantrucas", "Charquican", "Cochayuyo"]
    
    return render(request, 'index.html', context={'nombre_usuario':nombre, 'comidas':lista})

#CREAR EL DE LANZAMIENTOS