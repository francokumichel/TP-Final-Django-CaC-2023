from django.contrib import admin

# Register your models here.
from .models import Super, Responsable, TCU, Usuario

admin.site.register(Super)
admin.site.register(Responsable)
admin.site.register(TCU)
admin.site.register(Usuario)