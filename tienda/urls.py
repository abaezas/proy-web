from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('productos', views.productos, name = 'productos'),
    path('producto/<id>', views.producto, name = 'producto'),
    path('checkout', views.checkout, name = 'checkout'),
]
