from django.urls import path
from .views import home, LanzamientoZapatillas, Ver, form_aportes, form_mod_zapatillas, form_del_zapatillas

urlpatterns = [
    path('', home, name="home"),
    path('ver', Ver, name="ver"),
    path('LanzamientoZapatillas', LanzamientoZapatillas, name="LanzamientoZapatillas"),
    path('form_aportes', form_aportes, name="form_aportes"),
    path('form_mod_zapatillas/<id>', form_mod_zapatillas, name="form_mod_zapatillas"),
    path('form_del_zapatillas/<id>', form_del_zapatillas, name="form_del_zapatillas"),
]