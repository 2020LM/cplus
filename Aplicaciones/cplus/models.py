from django.db import models

class Pelicula(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length = 500)
    enCartelera = models.BooleanField(True)
    genero = models.CharField(max_length = 500)
    duración = models.CharField(max_length = 500)
    nacionalidad = models.CharField(max_length = 500)

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.IntegerField()
    nombre = models.CharField(max_length=500)
    apellido = models.CharField(max_length=500)
    monedasVIP = models.IntegerField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=500)
    nombre = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=2000)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, null = True, blank = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=500)

    def __str__(self):
        return self.nombre





class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    AsientosDisponibles = models.IntegerField()
    AsientosOcupados = models.IntegerField()
    NumeroDeAsientos = models.IntegerField()
    def __str__(self):
        return str(self.AsientosDisponibles)



class Funcion(models.Model):

    id = models.AutoField(primary_key=True)
    fecha = models.DateField(max_length=500)
    hora = models.TimeField(max_length=500)

    def __str__(self):
        return str(self.id)
    sucursal= models.ForeignKey(Sucursal, null = True, blank = True, on_delete = models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, null = True, blank = True, on_delete = models.CASCADE)
    sala = models.ForeignKey(Sala, null = True, blank = True, on_delete = models.CASCADE)



class Funcion2(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(max_length=500, default='Hola')
    hora = models.TimeField(max_length=500, default='Hola')
    sucursal = models.ForeignKey(Sucursal, null=True, blank=True, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, null=True, blank=True, on_delete=models.CASCADE)
    Sala = models.ForeignKey(Sala, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.id



class Entrada(models.Model):
    id = models.AutoField(primary_key=True)
    precio = models.IntegerField()
    descuento = models.IntegerField()
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    funcion = models.ForeignKey(Funcion, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cliente)

class Productovip(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=500)
    nombre = models.CharField(max_length=500)
    descripcion = models.CharField(max_length=2000)
    precio = models.IntegerField()
    cantidad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, null = True, blank = True, on_delete = models.CASCADE)

    def __str__(self):
        return self.nombre

