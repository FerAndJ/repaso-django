from django.urls import path, include #indicarle como crear un camino a django, el include le agregamos
from .views import index, plantilla

urlpatterns = [
    path('', index, name='index'),   #para que funcione hay que conectarlo al urls de proyecto django
    path('plantilla/', plantilla, name ='plantilla'),
]

