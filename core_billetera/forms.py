from django import forms

class medioPagoForm(forms.Form):
    tarjetaNumero = forms.CharField(label='Numero de la Tarjeta', max_length=16, required=True)
    correo = forms.EmailField(label='Correo Electrónico')
   # vto=forms.ChoiceField(label='Fecha Vto', max_length=16, required=True)
    nombre=forms.CharField(label='Nombre', max_length=100, required=False)
    #tipoTC=forms.ModelMultipleChoiceField(label='Tipo')
    
class supermercadoForm(forms.Form):
    nombre=forms.CharField(label='Nombre del Super', max_length=50, required=True)
    domicilio=forms.CharField(label='Domicilio')
    
    

