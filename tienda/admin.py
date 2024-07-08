from django.contrib import admin
from .models import tipoProducto, Producto

# Register your models here.

admin.site.register(tipoProducto)
admin.site.register(Producto)