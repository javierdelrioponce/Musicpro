from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
def index(request):
    return render(request, "blogapp/index.html")

def compra(request):
    return render(request, "blogapp/compra.html")

def cuerdas(request):
    return render(request, "blogapp/cuerdas.html")

def accesorios(request):
    return render(request, "blogapp/accesorios.html")

def amplificadores(request):
    return render(request, "blogapp/amplificadores.html")

def percusion(request):
    return render(request, "blogapp/percusion.html")

def menu(request):
    return render(request, "blogapp/menu.html")
