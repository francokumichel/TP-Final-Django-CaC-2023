from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view

urlpatterns = [
    #path('', views.index, name='inicio'),
    path('po', views.index, name='index'),
    
    path('accounts/login/', auth_views.LoginView.as_view(template_name='./core/login.html'),name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('login/', login_view, name='login'),
        
    path('mdp', views.mdp, name='mdp'),
    path('promo', views.promo, name='promo'),
    path('super', views.super, name='super'),
    path('estadistica', views.estadistica, name='estadistica'),
    path('medioPago', views.medioPago, name='medioPago'),
    path('supermercados', views.supermercados, name='supermercados'),
    path('maestroPagos', views.maestroPagos, name='maestroPagos'),
    path('mostrar_mensaje', views.mostrar_mensaje, name='mostrar_mensaje'),
    path('tipo_cobro', views.tipo_cobro, name='tipo_cobro'),
    path('edicionCobro/<id>', views.edicionCobro, name='edicionCobro'),
    path('editarCobro/<id>', views.editarCobro, name='editarCobro'),
    path('eliminarCobro/<id>', views.eliminarCobro, name='eliminarCobro'),
    path('usuarioTC/<id>', views.usuarioTC, name='usuarioTC'),
    
    path('AltaSuper', views.SuperCreateView.as_view(), name="AltaSuper"),
    path('superList', views.SuperListView.as_view(), name="superList"),
    path('responsable', views.ResponsableCreateView.as_view(), name="responsable"),   
    path('responsableList', views.ResponsableListView.as_view(), name="responsableList"), 
    path('tcu', views.TCUCreateView.as_view(), name="tcu"),   
    path('tcuList', views.TCUListView.as_view(), name="tcuList"),
    path('usuario', views.UsuarioCreateView.as_view(), name="usuario"),   
    path('usuarioList', views.UsuarioListView.as_view(), name="usuarioList"),    
    #path('docentes/listado', views.DocenteListView.as_view(), name="docentes_listado"),
    

]