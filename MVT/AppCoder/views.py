from django.shortcuts import render
from .models import Familiares
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def familiares(request):
    familiar=Familiares(nombre='Mercedez', dni=17000021,cumpleaños='1984-08-22')
    familiar.save()
    familiar1=Familiares(nombre='Carlos', dni=18567298,cumpleaños='1973-07-21')
    familiar1.save()
    familiar2=Familiares(nombre='Alejandra', dni=32567432,cumpleaños='1965-12-12')
    familiar2.save()
    diccionario={'Nombre':familiar.nombre,'Dni':familiar.dni,'Cumpleaños':familiar.cumpleaños,
                'Nombre1':familiar1.nombre,'Dni1':familiar1.dni,'Cumpleaños1':familiar1.cumpleaños,
                'Nombre2':familiar2.nombre,'Dni2':familiar2.dni,'Cumpleaños2':familiar2.cumpleaños
                }
    return render(request,"template1.html",diccionario)

def inicio(request):
    return render(request,"template_inicio.html")
    
