from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse
from datetime import datetime
import getpass
from .forms import medioPagoForm, supermercadoForm, maestroPagosForm, promoSuper, cobro_Form, promoSuper1
from .models import Supermercado, MedioPago, TipoCobro

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
    promoSuper_form = promoSuper()
    promoSuper1_form = promoSuper1()
    context = {
        'nombre_usuario': usuario,
        'fecha': datetime.now(),
        'es_instructor': True,
        'form': promoSuper_form,
        'form1': promoSuper1_form
    }
    return render(request, "core/promo.html", context)

def super(request):
    usuario=getpass.getuser
    context = {
        'nombre_usuario': usuario,
        'fecha': datetime.now(),
        'es_instructor': True,
        'cursos': w_supermercados,
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
    medioPago_form = medioPagoForm()
    context = {
        'nombre_usuario': usuario,
        'fecha': datetime.now(),
        'es_instructor': True,
        'form': medioPago_form,
    }
    return render(request, 'core/mdp.html', context)

def supermercados(request):

    if request.method == "POST":
        supermercados_form = supermercadoForm(request.POST)
        if supermercados_form.is_valid():
           # Dar de alta la info
            write_supermercados=Supermercado(super_name=request.POST['nombre'],super_direccion=request.POST['domicilio'])
            write_supermercados.save()
            titulo = "Felicitaciones"
            mensaje = "La consulta se ha enviado con éxito."
            icono = "success"   
            messages.success(request, "Grabado correctamente")
            return redirect(reverse('supermercados'))   
        else:
            titulo = "ERROR"
            mensaje = "Revise los datos ingresados."
            icono = "error" 
            mensaje = "felicitaciones|cargo correctamente|error"
            mi_diccionario = {
                        'titulo': "Revise los datos ingresados.",
                        'texto': "parametro2",
                        'icon': "error",
                    }
            contexto = {
                        'mi_diccionario': mi_diccionario,
            }
            messages.error(request, contexto)
            #messages.error(request, "felicitaciones|cargo correctamente|error") 
            return redirect(reverse('supermercados'))                  
    else:
        usuario=getpass.getuser
        supermercados_dict1 = Supermercado.objects.all()
        supermercados_form = supermercadoForm()

        context = {
            'nombre_usuario': usuario,
            'fecha': datetime.now(),
            'es_instructor': True,
            'form': supermercados_form,
            'cursos': supermercados_dict1
        }
        return render(request, 'core/super.html', context)

def maestroPagos(request):
      
    usuario=getpass.getuser
    maestroPagos_form = maestroPagosForm()
    context = {
        'nombre_usuario': usuario,
        'fecha': datetime.now(),
        'es_instructor': True,
        'form': maestroPagos_form,
    }
    return render(request, 'core/mdp.html', context)

def mostrar_mensaje(request):
    message = "Este es un mensaje de información."
    return render(request, 'message_template.html', {'message': message})


def tipo_cobro(request):

    if request.method == "POST":
        tipo_cobroFrom = cobro_Form(request.POST)
        if tipo_cobroFrom.is_valid():
           # Dar de alta la info
            write_TipoCobro=TipoCobro(pago_name =request.POST['pago_name'])
            write_TipoCobro.save()
            titulo = "Felicitaciones"
            mensaje = "La consulta se ha enviado con éxito."
            icono = "success"   
            messages.success(request, "Grabado correctamente")
            return redirect(reverse('tipo_cobro'))   

        else:
            titulo = "ERROR"
            mensaje = "Revise los datos ingresados."
            icono = "error" 
            mensaje = "felicitaciones|cargo correctamente|error"
            mi_diccionario = {
                        'titulo': "Revise los datos ingresados.",
                        'texto': "parametro2",
                        'icon': "error",
                    }
            contexto = {
                        'mi_diccionario': mi_diccionario,
            }
            messages.error(request, contexto)
            #messages.error(request, "felicitaciones|cargo correctamente|error") 
            return redirect(reverse('tipo_cobro'))                  
    else:
        usuario=getpass.getuser
        tipoCobroList = TipoCobro.objects.all()
        tipo_cobro = cobro_Form()

        context = {
            'nombre_usuario': usuario,
            'fecha': datetime.now(),
            'es_instructor': True,
            'form': tipo_cobro,
            'cursos': tipoCobroList
        }
        return render(request, 'core/tipo_cobro.html', context)
        #return redirect(reverse('tipo_cobro'))
    
def edicionCobro(request,id):
            cursor= TipoCobro.objects.get(id=id)
            tipo_cobro=cursor
            context = {
              #  'nombre_usuario': usuario,
                'fecha': datetime.now(),
                'es_instructor': True,
                'form': cursor,
            }
            return render(request, 'core/edicionCobro.html', {"curso":cursor})
           #return redirect(reverse('edicionCobro'))

def editarCobro(request,id):
    cursor= TipoCobro.objects.get(id=id)
    if request.method == "POST":
        #id = int(request.POST.get('txtpago_id'))
        w_pago_name = request.POST.get('txtpago_name')
        cursor= TipoCobro.objects.get(id=id)
        cursor.pago_name=w_pago_name
        cursor.save()
        tipoCobroList = TipoCobro.objects.all()        
        context = {
            #'nombre_usuario': usuario,
            'fecha': datetime.now(),
            'es_instructor': True,
            'form': tipo_cobro,
            'cursos': tipoCobroList
        }
        #return render(request, 'core/tipo_cobro.html', context)
        return render(request, "core/index.html", context)


def eliminarCobro(request,id):
    curso= TipoCobro.objects.get(id=id)
    curso.delete()
    titulo = "Broorado con exito"
    mensaje = "La consulta se ha enviado con éxito."
    icono = "success"   
    messages.success(request, "Borrado correctamente")
    usuario=getpass.getuser
    tipoCobroList = TipoCobro.objects.all()
    tipo_cobro = cobro_Form()

    context = {
            'nombre_usuario': usuario,
            'fecha': datetime.now(),
            'es_instructor': True,
            'form': tipo_cobro,
            'cursos': tipoCobroList
        }
    return render(request, 'core/tipo_cobro.html', context)



#def contacto(request):
#    if request.method == "POST":
#        # Instanciamos un formulario con datos
#        formulario = ContactoForm(request.POST)
#
#        # Validarlo
#        if formulario.is_valid():
#            # Dar de alta la info
#
#            messages.info(request, "Consulta enviada con éxito")
#            return redirect(reverse("alumnos_listado"))#
#
 #   else: # GET
#        formulario = ContactoForm()
#
#    context = {
#        'contacto_form': formulario
 #   }
#
#    return render(request, "core/contacto.html", context)
