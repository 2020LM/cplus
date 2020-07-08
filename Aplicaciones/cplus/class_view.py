from django.shortcuts import render,redirect
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
from  django.urls import reverse_lazy
from .forms import PeliculaForm,ProductoForm,FuncionForm,ProductovipForm
from .models import Pelicula,Entrada,Cliente,Sala,Producto,Funcion,Productovip
from tkinter import messagebox


class PeliculaList(ListView):
    model = Pelicula
    template_name = 'index2.html'

class PeliculaList2(ListView):
    model = Pelicula
    template_name = 'modificar_o_eliminar_pelicula.html'

class PeliculaCreate(CreateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'crear_pelicula.html'
    success_url = reverse_lazy('index2')

class PeliculaUptate(UpdateView):
    model = Pelicula
    form_class = PeliculaForm
    template_name = 'modificar_pelicula.html'
    success_url = reverse_lazy('index2')

class PeliculaDelete(DeleteView):
    model = Pelicula
    template_name = 'eliminar_pelicula.html'
    success_url = reverse_lazy('index2')

class FuncionList(ListView):
    model = Funcion
    template_name = 'funciones.html'

class ProductoList(ListView):
        model = Producto
        template_name = 'productos.html'

class MostrarProductoList(DeleteView):
    model = Producto
    template_name = 'carameleria.html'

class FuncionesList(ListView):
    model = Funcion
    template_name = 'funciones.html'

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'crear_producto.html'
    success_url = reverse_lazy('productos')

class ProductoList2(ListView):
    model = Producto
    template_name = 'modificar_o_eliminar_producto.html'

class ProductoUptate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'modificar_producto.html'
    success_url = reverse_lazy('modificar_o_eliminar_producto')

class ProductoDelete(DeleteView):
    model = Producto
    template_name = 'eliminar_producto.html'
    success_url = reverse_lazy('modificar_o_eliminar_producto')

class FuncionList(ListView):
    model = Funcion
    template_name = 'funcionesf.html'

class FuncionCreate(CreateView):
    model = Funcion
    form_class = FuncionForm
    template_name = 'crear_funcion.html'
    success_url = reverse_lazy('funcionesf')

class FuncionList2(ListView):
    model = Funcion
    template_name = 'modificar_o_eliminar_funcion.html'

class FuncionUptate(UpdateView):
    model = Funcion
    form_class = FuncionForm
    template_name = 'modificar_funcion.html'
    success_url = reverse_lazy('modificar_o_eliminar_funcion')

class EliminarFuncion(DeleteView):
    model = Funcion
    template_name = 'eliminar_funcion.html'
    success_url = reverse_lazy('modificar_o_eliminar_funcion')

class ComprarEntrada(DeleteView):
    model = Funcion
    template_name = 'entrada.html'
    success_url = reverse_lazy('funcionesf')

class ProductoVIPList(ListView):
    model = Productovip
    template_name = 'productos_VIP.html'

class MostrarProductoVIPList(DeleteView):
    model = Productovip
    template_name = 'carameleria_VIP.html'

class ProductovipCreate(CreateView):
    model = Productovip
    form_class = ProductovipForm
    template_name = 'crear_productovip.html'
    success_url = reverse_lazy('productos_VIP')

class ProductovipList2(ListView):
    model = Productovip
    template_name = 'modificar_o_eliminar_productovip.html'


class ProductovipUptate(UpdateView):
    model = Productovip
    form_class = ProductovipForm
    template_name = 'modificar_productovip.html'
    success_url = reverse_lazy('modificar_o_eliminar_productovip')

class ProductovipDelete(DeleteView):
    model = Productovip
    template_name = 'eliminar_productovip.html'
    success_url = reverse_lazy('modificar_o_eliminar_productovip')