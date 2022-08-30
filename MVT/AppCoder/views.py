from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def familiares(request):
    familiar=Familiares(nombre='Augusto', dni=40123321,cumpleaños='1999-05-22')
    familiar.save()
    familiar1=Familiares(nombre='Juan', dni=19449990,cumpleaños='1945-07-21')
    familiar1.save()
    familiar2=Familiares(nombre='Augusto', dni=40123321,cumpleaños='1969-01-14')
    familiar2.save()
    diccionario={'Nombre':familiar.nombre,'Dni':familiar.dni,'Cumpleaños':familiar.cumpleaños,
                'Nombre1':familiar1.nombre,'Dni1':familiar1.dni,'Cumpleaños1':familiar1.cumpleaños,
                'Nombre2':familiar.nombre,'Dni2':familiar2.dni,'Cumpleaños2':familiar2.cumpleaños
                }
    plantilla=loader.get_template('template1.html')
    documento=plantilla.render(diccionario)
    return HttpResponse(documento)