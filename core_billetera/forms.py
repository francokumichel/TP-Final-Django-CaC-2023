from django import forms
from django.forms import widgets
from django.contrib import messages
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .models import Super



class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

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


supermercados_dict = {
    '01': 'Disco',
    '02': 'Jumbo',
    '03': 'Coto',
}

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
    
    def clean(self):
        
        # Este if simula una busqueda en la base de datos
        if self.cleaned_data["nombre"] == "Carlos":
            #messages.info(request, "Consulta enviada con éxito")
            raise ValidationError("El usuario Carlos Lopez ya existe")
        
        # Si el usuario no existe lo damos de alta

        return self.cleaned_data


   
  
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
        
#        def clean_edad(self):
#            if self.cleaned_data["edad"] < 18:
#                raise ValidationError("El usuario no puede tener menos de 18 años")
#        
#            return self.cleaned_data["edad"]
    
    
class promoSuper(forms.Form):
#    eleccionSuper= forms.CharField(label='Selecciona Super', widget=forms.Select(choices=w_supermercados))
#    eleccionTC= forms.CharField(label='Selecciona TC', widget=forms.Select(choices=w_nombreTC))
    eleccionSuper= forms.CharField(label='Selecciona Super', widget=forms.Select(choices=w_supermercados))
    eleccionTC= forms.CharField(label='Selecciona TC', widget=forms.Select(choices=w_nombreTC))
    
class promoSuper1(forms.Form):
    eleccionSuper1= forms.CharField(
        label=' Super',
        widget=forms.TextInput(attrs={'placeholder': 'supermercado', 'class': 'fondo_rojo'})
        
        )
    eleccionTC1= forms.CharField(label=' TC')  
    
class cobro_Form(forms.Form):
    pago_name = forms.CharField(label='Nombre de Pago',
                             max_length=30,
                             required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Nombre Forma de Pago'}))
       
        
    
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
         
class altaSuperModelForm(forms.ModelForm):
    class Meta:
        model = Super
        fields = '__all__'
        widgets={
            'super_name': forms.Textarea(attrs={'col':20, 'rows':20})
        }

        

# Esto es para ver que pasa si funciona o no
    def clean_cuit(self):
        cuit = self.cuit.strip() # Eliminar espacios en blanco al principio y al final

        if not cuit.isdigit():
            raise ValidationError("El CUIT debe contener solo dígitos.")

        if len(cuit) != 11:
            raise ValidationError("El CUIT debe tener 11 dígitos.")
        
        self.changed_data['cuit'] = cuit
        return self.changed_data['cuit']
  
# Modifica Supermercado
class SuperForm(forms.ModelForm):
    class Meta:
        model = Super
        fields = '__all__'
