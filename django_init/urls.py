"""django_init URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Aplicaciones.principal.views import inicio,crearPersona,editarPersona,eliminarPersona
from Aplicaciones.principal.class_view import PersonaList, PersonaCreate, PersonaUptate, PersonaDelete
from Aplicaciones.cplus.class_view import PeliculaList, PeliculaCreate, PeliculaUptate, PeliculaDelete, PeliculaList2,FuncionList, ProductoList, MostrarProductoList,ProductoCreate,ProductoList2,ProductoUptate,ProductoDelete,FuncionCreate,FuncionesList,FuncionList2,FuncionUptate,EliminarFuncion,ComprarEntrada,ProductoVIPList,MostrarProductoVIPList,ProductovipCreate,ProductovipList2,ProductovipUptate,ProductovipDelete
from Aplicaciones.cplus.views import MostrarProductoList2,FindUser


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PeliculaList.as_view(), name= 'index2'),
    path('crear_persona/',PersonaCreate.as_view(), name= 'crearPersona'),
    path('editar_persona/<int:pk>/',PersonaUptate.as_view(),name = 'editar_persona'),
    path('eliminar_persona/<int:pk>/',PersonaDelete.as_view(),name = 'eliminar_persona'),
    path('crear_pelicula/',PeliculaCreate.as_view(),name = 'crear_pelicula'),
    path('modificar_o_eliminar_pelicula/',PeliculaList2.as_view(), name= 'modificar_o_eliminar_pelicula'),
    path('modificar_pelicula/<int:pk>',PeliculaUptate.as_view(), name= 'modificar_pelicula'),
    path('eliminar_pelicula/<int:pk>',PeliculaDelete.as_view(), name= 'eliminar_pelicula'),
    path('funciones/<int:pk>', FuncionList.as_view(), name= 'funciones'),
    path('productos/', ProductoList.as_view(), name= 'productos'),
    path('carameleria/<int:pk>', MostrarProductoList.as_view(), name='carameleria'),
    path('funciones/productos/crear_producto', ProductoCreate.as_view(), name='crear_producto'),
    path('funciones/productos/modificar_o_eliminar_producto/', ProductoList2.as_view(), name='modificar_o_eliminar_producto'),
    path('funciones/productos/modificar_o_eliminar_producto/<int:pk>', ProductoUptate.as_view(), name='modificar_producto'),
    path('eliminar_producto/<int:pk>',ProductoDelete.as_view(), name= 'eliminar_producto'),
    path('funcionesf/',FuncionList.as_view(), name= 'funcionesf'), #funcionesf son las funciones verdaderas
    path('crear_funcion/', FuncionCreate.as_view(), name='crear_funcion'),
    path('modificar_o_eliminar_funcion/',FuncionList2.as_view(),name='modificar_o_eliminar_funcion'),
    path('modificar_funcion/<int:pk>',FuncionUptate.as_view(),name='modificar_funcion'),
    path('eliminar_funcion/<int:pk>',EliminarFuncion.as_view(),name='eliminar_funcion'),
    path('entrada/<int:pk>', ComprarEntrada.as_view(), name='entrada'),
    path('entrada/FindUser', FindUser, name='entrada'),
    path('productos_VIP/', ProductoVIPList.as_view(), name= 'productos_VIP'),
    path('carameleria_VIP/<int:pk>', MostrarProductoVIPList.as_view(), name= 'carameleria_VIP'),
    path('productos_VIP/crear_productovip', ProductovipCreate.as_view(), name= 'crear_productovip'),
    path('modificar_o_eliminar_productovip/', ProductovipList2.as_view(), name='modificar_o_eliminar_productovip'),
    path('modificar_productovip/<int:pk>', ProductovipUptate.as_view(), name='modificar_productovip'),
    path('eliminar_productovip/<int:pk>', ProductovipDelete.as_view(), name='eliminar_productovip'),
]
