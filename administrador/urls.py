from django.urls import path
from . import views

urlpatterns = [
    path('inicioAdmin', views.inicioAdmin, name = 'inicioAdmin'),
    path('agregarProd', views.agregarProd, name = 'agregarProd'),
    path('listarProd', views.listarProd, name = 'listarProd'),
    path('modProd/<id>', views.modProd, name = 'modProd'),
    path('eliminarProd/<id>', views.eliminarProd, name = 'eliminarProd'),
]