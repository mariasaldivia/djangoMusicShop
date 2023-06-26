from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'tienda/index.html')

def artistas(request):
    return render(request,'tienda/artista.html')

def signUp(request):
    return render(request,'tienda/registro.html')

def signIn(request):
    return render(request,'tienda/login.html')

def ub(request):
    return render(request,'tienda/ubicacion.html')

def producto(request):
    return render(request,'tienda/productos.html')