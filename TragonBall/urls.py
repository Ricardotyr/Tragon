from django.urls import path
from . import views

app_name = "TragonBall"

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('registrarse', views.registroCliente, name="reg"),
    path('iniciarsesion', views.paginaLogin, name='paginaLogin'),
    path('cerrarSesion', views.cerrarSesion, name='cerrarSesion'),
    path('contacto/', views.contacto, name="contacto"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('tiposPago', views.tiposPago, name="tiposPago"),
    path('delivery', views.delivery, name="delivery"),
    path('producto', views.producto, name="producto"),
    path('promocion', views.promocion, name="promocion"),
    path('carro', views.carro, name="carro"),
    path('comprar', views.comprar, name="comprar"),
     path('comprahecha', views.comprahecha, name="comprahecha"),
    #path('sucess/', views.sucess, name="sucess"),
    #path('mycart/', views.simple_checkout, name="simple"),
    
]