from django.shortcuts import render

# Create your views here.

def carrito_main(request):
    return render(request, "carrito_main.html", {})

def carrito_agregar(request):
    pass

def carrito_borrar(request):
    pass

def carrito_modificar(request):
    pass