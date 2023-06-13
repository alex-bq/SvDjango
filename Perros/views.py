from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Mascota, Perros

# Create your views here.


def index(request):
    return render(request, "index.html")


def api(request):
    return render(request, "api.html")


def Donaciones(request):
    return render(request, "Donaciones.html")


def formulario(request):
    return render(request, "formulario.html")


def perros(request):
    return render(request, "perros.html")


def primerSaludo(request):
    return HttpResponse("primer saludito hola buenas tardes")


def mostrarNombre(request, nombre):
    documento = """<html><body><h1>Se ha ingresado a: %s</h1></body></html>""" % nombre
    return HttpResponse(documento)


def calcularEdad(request, ano):
    edadActual = 19
    periodo = ano - 2023
    edadFutura = edadActual + periodo

    documento = (
        """<html><body><h1> en el ano : %s tendras %s anos </h1></body></html>"""
        % (ano, edadFutura)
    )
    return HttpResponse(documento)


def index2(request):
    listaMateria = ["HTML", "CSS", "JS", "DJANGO", "PYTHON"]
    context = {"nombre": "poto", "materia": listaMateria}
    return render(request, "index.html", context)


def crud(request):
    perros = Perros.objects.all()
    context = {"perros": perros}
    return render(request, "perros/perros_list.html", context)
