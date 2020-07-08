from django import forms
from .models import Pelicula, Producto,Cliente,Entrada,Sala ,Funcion,Productovip

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

class FuncionForm(forms.ModelForm):
    class Meta:
        model = Funcion
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('cedula',)

class ProductovipForm(forms.ModelForm):
    class Meta:
        model = Productovip
        fields = '__all__'

