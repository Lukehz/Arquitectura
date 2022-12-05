from django.shortcuts import render

# Create your views here.
def Formulario(request):
    return render(request, "../templates/formulario.html")

def Inicio(request):
    return render(request, "../templates/index.html")

def Servicios(request):
    return render(request, "../templates/servicios.html")

def Productos(request):
    return render(request, "../templates/productos.html")