from django.urls import path
from .views import home, Ver

urlpatterns = [
    path('', home, name="home"),
    path('ver', Ver, name="ver"),
]