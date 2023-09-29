from django import forms
from django.forms import widgets

MES_CHOICES = [
        ('01', 'Enero'),
        ('02', 'Febrero'),
        ('03', 'Marzo'),
        # Agrega más meses aquí
    ]

ANIO_CHOICES = [
        ('2023', '2023'),
        ('2024', '2024'),
        ('2025', '2025'),
        # Agrega más años aquí
    ]

w_supermercados = [
        ('01', 'Disco'),
        ('02', 'Jumbo'),
        ('03', 'Coto'),
        # Agrega más meses aquí
    ]

w_nombreTC = [
        ('01', 'Visa'),
        ('02', 'Master'),
        ('03', 'AMEX'),
        # Agrega más meses aquí
    ]

# CRUD Medios de Pago del Usuario
class medioPagoForm(forms.Form):
  
    tarjetaNumero = forms.CharField(
        label='Numero de la Tarjeta',
        max_length=16,
        required=True,
        widget=widgets.NumberInput(attrs={'class': 'ver1', 'inputmode': 'numeric'})
    )
    correo = forms.EmailField(label='Correo Electrónico')
 #   vto = forms.ChoiceField(
 #       label='Fecha de Vencimiento',
 #       required=True,
 #       choices=[
 #           (mes, mes) for mes in MES_CHOICES
 #       ] + [
 #           (anio, anio) for anio in ANIO_CHOICES
 #       ]
 #   )
    nombre=forms.CharField(label='Nombre', max_length=100, required=False)
    #tipoTC=forms.ModelMultipleChoiceField(label='Tipo')
    
#CRUD de Tabla Supermercado tiene asociado CRUD tabla Masterpago
class supermercadoForm(forms.Form):
    nombre=forms.CharField(label='Supermercado', max_length=50, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Nombre de Supermercado'}))
    domicilio=forms.CharField(label='Domicilio', max_length=50, required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Domicilio Supermercado'}))
    
  
#CRUD de Tabla MasterPago detalla formas de cobro    
class maestroPagosForm(forms.Form):
        nombre=forms.CharField(label='Nombre de Pago',
                             max_length=50,
                             required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Nombre Forma de Pago'})),
        tipo = forms.ChoiceField(
            label='Tipo',
            required=True,
            choices=[
            (w_tipo, w_tipo) for w_tipo in w_nombreTC
            ]),      
    
    
class promoSuper(forms.Form):
    eleccionSuper= forms.CharField(label='Selecciona Super', widget=forms.Select(choices=w_supermercados))
    eleccionTC= forms.CharField(label='Selecciona TC', widget=forms.Select(choices=w_nombreTC))
    
class promoSuper1(forms.Form):
    eleccionSuper1= forms.CharField(label=' Super', widget=forms.Select(choices=w_supermercados))
    eleccionTC1= forms.CharField(label=' TC', widget=forms.Select(choices=w_nombreTC))    
        
    
# Pro favor no borrar hasta ver terminado el TP    
#   vto = forms.ChoiceField(
#       label='Fecha de Vencimiento',
#       required=True,
#      choices=[
#       (w_super, w_super) for w_super in w_supermercados
#       ]),
#   w_nombres1 = forms.ChoiceField(
#       label='Fecha de Vencimiento',
#       required=True,
#      choices=[
#       (w_nombres, w_nombres) for w_nombres in w_nombreTC
#       ])      
         
   
  

