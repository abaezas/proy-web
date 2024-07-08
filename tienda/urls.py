from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'inicio'),
    path('productos', views.productos, name = 'productos'),
    path('carrito', views.carrito, name = 'carrito'),
]
