from django.db import models

# Create your models here.
class Supermercado(models.Model):
    super_name = models.CharField(max_length=30, verbose_name='Nombre Supermercado')
    super_direccion = models.CharField(max_length=30, verbose_name='Direccion Supermercado')
    super_mail = models.EmailField(max_length=50, unique=True, verbose_name='Mail del Supermercado')
    super_telefono = models.CharField(max_length=50, verbose_name='Telefono')
    
    class Meta:
        abstract = True    
    
class TipoCobro(Supermercado):
    pago_name = models.CharField(max_length=30, verbose_name='Tipo de Cobro')

class Super(Supermercado):
    cuit = models.IntegerField(verbose_name="cuit", unique=True)
    
    def __str__(self):
        return self.super_name  # Suponiendo que 'nombre' es un campo en tu modelo 'Super'    

    
class Persona(models.Model):
    persona_name = models.CharField(max_length=50, verbose_name='Nombre')
    persona_apellido = models.CharField(max_length=50, verbose_name='Apellido')    
    persona_direccion = models.CharField(max_length=50, verbose_name='Direccion')
    persona_mail = models.EmailField(max_length=50, unique=True, verbose_name='Mail Personal')
    persona_telefono = models.CharField(max_length=50, verbose_name='Telefono Personal')    
    
    class Meta:
        abstract = True  
class Responsable(Persona):
    super = models.ForeignKey(Super, on_delete=models.CASCADE)
    responsable_mail= models.EmailField(max_length=50, unique=True, verbose_name='Mail del Responsable')
    responsable_telefono = models.CharField(max_length=50, verbose_name='Telefono')
    cuil = models.IntegerField(verbose_name="cuil", unique=True)
    
    def __str__(self):
        linea=self.persona_name, self.persona_apellido, self.persona_mail, self.super
        return self.linea 
    
class Usuario(Persona):
        pass
    
class MedioPago(models.Model):
    mp_tipo = models.CharField(max_length=30, verbose_name='Tipo de Pago')
    mp_nombre = models.CharField(max_length=30, verbose_name='Nombre de Pago')
    mp_numero = models.IntegerField(verbose_name='Numero Tarjeta')
    mp_codigo = models.CharField(max_length=30, verbose_name='Codigo')
    mp_fvto = models.CharField(max_length=4, verbose_name='Vto') 
    
class Compra(models.Model):
    mp_fvto = models.DateField()
    mp_ID_Super = models.IntegerField()
    mp_TotalSinDto = models.IntegerField()
    mp_TotalConDto = models.IntegerField()

     


    
    