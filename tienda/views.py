from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import prodForm

# Create your views here.
def home(request):

    productos = Producto.objects.all()
    context = {
        'producto' : productos
    }

    return render(request, 'tienda/inicio.html', context)

def productos(request):
    
    productos   = Producto.objects.all()
    
    
    tipos       = tipoProducto.objects.all()

    context     = {
        'productos' : productos,
        'tipos'     : tipos    
    }

    return render(request, 'tienda/productos.html', context)

def carrito(request):
    return render(request, 'tienda/carrito.html')

