from django.urls import path
from . import views

urlpatterns = [
    path('', views.carrito_main, name='carrito_main'),
    path('agregar/', views.carrito_agregar, name='carrito_agregar'),
    path('delete/', views.carrito_borrar, name='carrito_borrar'),
    path('modificar/', views.carrito_modificar, name='carrito_modificar'),
]