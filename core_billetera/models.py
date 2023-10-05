from django.db import models

# Create your models here.

class TipoCobro(models.Model):
    pago_name = models.CharField(max_length=30)

class Supermercado(models.Model):
    super_name = models.CharField(max_length=30)
    super_direccion = models.CharField(max_length=30)
    
class MedioPago(models.Model):
    mp_tipo = models.CharField(max_length=30)
    mp_nombre = models.CharField(max_length=30)
    mp_numero = models.IntegerField()
    mp_codigo = models.CharField(max_length=30)
    mp_fvto = models.CharField(max_length=4) 
    
class Compra(models.Model):
    mp_fvto = models.DateField()
    mp_ID_Super = models.IntegerField()
    mp_TotalSinDto = models.IntegerField()
    mp_TotalConDto = models.IntegerField()

     


    
    