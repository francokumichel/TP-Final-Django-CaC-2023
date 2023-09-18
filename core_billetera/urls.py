from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('mdp', views.mdp, name='mdp'),
    path('promo', views.promo, name='promo'),
    path('super', views.super, name='super'),
    path('estadistica', views.estadistica, name='estadistica')

]