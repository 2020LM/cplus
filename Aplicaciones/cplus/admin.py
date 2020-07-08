from django.contrib import admin
from .models import Pelicula, Cliente, Producto,Entrada,Sala,Sucursal,Funcion,Productovip



admin.site.register(Pelicula)
admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Entrada)
admin.site.register(Funcion)
admin.site.register(Sala)
admin.site.register(Sucursal)
admin.site.register(Productovip)

