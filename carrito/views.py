from django.shortcuts import render, get_object_or_404
from .carrito import Carrito
from tienda.models import Producto
from django.http import JsonResponse

# Create your views here.

def carritoMain(request):
    return render(request, "carrito_main.html", {})

def carritoAgregar(request):
    
    carrito = Carrito(request)

    if request.POST.get('action') == 'post':
        producto_id = int(request.POST.get('producto.id'))
        
        producto = get_object_or_404(Producto, id=producto_id)
        carrito.add(producto=producto)

        respuesta = JsonResponse({'Nombre Producto: ': producto })

        return respuesta

def carritoBorrar(request):
    pass

def carritoModificar(request):
    pass