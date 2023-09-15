from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import getpass

def index(request):
    context = {
        'nombre_usuario': {getpass.getuser},
        'fecha': datetime.now(),
        'es_instructor': True,
    }
    return render(request, "core/index.html", context)