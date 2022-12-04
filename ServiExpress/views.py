from django.shortcuts import render

# Create your views here.
def Formulario(request):
    return render(request, "../templates/formulario.html")

def Inicio(request):
    return render(request, "../templates/index.html")