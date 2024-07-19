from django.urls import path
from . import views

urlpatterns = [
    path('', views.carritoMain, name='carritoMain'),
    path('agregar/', views.carritoAgregar, name='carritoAgregar'),
    path('delete/', views.carritoBorrar, name='carritoBorrar'),
    path('modificar/', views.carritoModificar, name='carritoModificar'),
]