from django.urls import path
from .views import home, Ver, form_aportes, form_mod_zapatillas

urlpatterns = [
    path('', home, name="home"),
    path('ver', Ver, name="ver"),
    path('form_aportes', form_aportes, name="form_aportes"),
    path('form_mod_zapatillas/<id>', form_mod_zapatillas, name="form_mod_zapatillas"),
]