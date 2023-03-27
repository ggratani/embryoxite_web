from django.shortcuts import render
from modelos.models import Producto

# Create your views here.

def modelos(request):

    productos=Producto.objects.all()

    return render(request, "modelos/modelos.html", {"productos":productos})

