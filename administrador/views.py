from django.shortcuts import render
from tienda.models import *
from tienda.forms import prodForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def inicioAdmin(request):
    return render(request, 'administrador/inicio_admin.html')

@login_required
def home(request):
    return render(request, 'administrador/home.html')

@login_required
def agregarProd(request):

    data = { 'form' : prodForm() }

    if request.method == 'POST' :
        formulario = prodForm(data = request.POST, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            data ['mensaje'] = 'Guardado correctamente'
        else:
            data['form'] = formulario

    return render(request, 'administrador/agregar.html', data)

@login_required
def listarProd(request):

    productos   = Producto.objects.all()

    context = {
        'productos' : productos
    }

    return render(request, 'administrador/listar.html', context)

@login_required
def modProd(request, id):

    producto = get_object_or_404(Producto, id = id)

    data = {'form' : prodForm(instance = producto)}

    if request.method == 'POST' :
        formulario = prodForm(data = request.POST, instance = producto, files = request.FILES)
        if formulario.is_valid():
            formulario.save()
            data ['mensaje'] = 'Modificar correctamente'
            return redirect(to = 'listarProd')

    return render(request, 'administrador/modificar.html', data)

@login_required
def eliminarProd(request, id):

    producto = get_object_or_404(Producto, id = id)
    producto.delete()

    return redirect(to = 'listarProd')