from django.urls import path
from .views import  home

urlpatterns=[ 
    path('', home, name="home"),
    # path('form_vehiculo', form_vehiculo, name="form_vehiculo"),
]