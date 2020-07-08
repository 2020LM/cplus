from django.db.models import Model

from .models import Pelicula, Producto,Entrada,Cliente,Funcion,Sala
from .forms import PeliculaForm,ClienteForm
from django.shortcuts import redirect,render
from django.views.generic import CreateView,DeleteView,ListView,UpdateView
import tkinter
from tkinter import messagebox


def MostrarProductoList2(DeleteView):

    model = Producto
    template_name = 'carameleria.html'
    precioTotal = {object.precio} * {object.cantidad}

    messagebox.showinfo("Alerta",
                        f"Ha decicido comprar {object.cantidad} {object.nombre} y el precio que se sumará a la cuenta final es:  {precioTotal}")


def FindUser(request,cedula):
    print(cedula)
    Model.objects.filter(atributo = cedula)
    messagebox.showinfo("Alerta",
                        f"Se han comprado correctamente las entradas")
    return('funcionesf')






