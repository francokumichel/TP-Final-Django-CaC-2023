from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import getpass
from .forms import medioPagoForm


def inicio(request):
    return render(request, "core/inicio.html")

def index(request):
    usuario=getpass.getuser
    context = {
        'nombre_usuario': usuario,
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, "core/index.html", context)

def estadistica(request):
    usuario=getpass.getuser
    context = {
        'nombre_usuario': usuario,
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, "core/estadistica.html", context)

def mdp(request):
    usuario=getpass.getuser
    context = {
        'nombre_usuario': usuario,
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, "core/mdp.html", context)

def promo(request):
    usuario=getpass.getuser
    context = {
        'nombre_usuario': usuario,
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, "core/promo.html", context)

def super(request):
    usuario=getpass.getuser
    context = {
        'nombre_usuario': usuario,
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, "core/super.html", context)

def medioPago(request):
   # if request.method == 'POST':
   #     contacto_form = ContactoForm(request.POST)
   #     if contacto_form.is_valid():
   #         # Procesa los datos aquí, por ejemplo, guárdalos en la base de datos
   #         nombre = contacto_form.cleaned_data['nombre']
   #        correo = contacto_form.cleaned_data['correo']
   #         # Realiza las acciones necesarias con los datos
    #else:
    usuario=getpass.getuser
    context = {
        'nombre_usuario': usuario,
        'fecha': datetime.now(),
        'es_instructor': True,
        'form': medioPago_form,
    }
    medioPago_form = medioPagoForm()
    
    return render(request, './core/mdp.html', context)
