from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def familiares(request):
    familiar=Familiares(nombre='Augusto', dni=40123321,cumpleaños='1999-05-22')
    familiar.save()
    diccionario={'Nombre':familiar.nombre,'Dni':familiar.dni,'Cumpleaños':familiar.cumpleaños}
    plantilla=loader.get_template('template1.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)