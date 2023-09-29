from django.urls import path, re_path
from . import views

urlpatterns = [
    #path('', views.index, name='inicio'),
    path('po', views.index, name='index'),
    path('mdp', views.mdp, name='mdp'),
    path('promo', views.promo, name='promo'),
    path('super', views.super, name='super'),
    path('estadistica', views.estadistica, name='estadistica'),
    path('medioPago', views.medioPago, name='medioPago'),
    path('supermercados', views.supermercados, name='supermercados'),
    path('maestroPagos', views.maestroPagos, name='maestroPagos')

]