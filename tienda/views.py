from django.shortcuts import render
from .models import Artista, Producto

# Create your views here.
def home(request):
    return render(request,'tienda/index.html')

def artistas(request):
    #SELECT * FROM ARTISTA
    artistas = Artista.objects.all()
    data = {"artistas":artistas}
    return render(request,'tienda/artista.html',data)

def signUp(request):
    return render(request,'tienda/registro.html')

def signIn(request):
    return render(request,'tienda/login.html')

def ub(request):
    return render(request,'tienda/ubicacion.html')

def producto(request):
    #SELECT * FROM PRODUCTO
    productos = Producto.objects.all()
    data = {"productos":productos}
    return render(request,'tienda/productos.html',data)
    
def agregar_producto(request):
    return render(request,'tienda/producto/agregar.html')