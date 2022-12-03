from email.message import EmailMessage
from django.shortcuts import render, redirect
from TragonBall.models import Cliente, ProductoElaborado, CompraPaypal
from django.contrib import messages
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, JsonResponse
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersGetRequest, OrdersCaptureRequest
import sys, json
from carro.carro import Carro
#import json,random,requests

# Create your views here.

# Inicio
def inicio(request):
    return render(request, "inicio.html")

# Productos
def producto(request):
    producto = ProductoElaborado.objects.filter(categoria_id_categoria__in = [4,5,6,7])
    return render(request,'productos.html', {"producto":producto})

# Promociones
def promocion(request):
    promocion = ProductoElaborado.objects.filter(categoria_id_categoria='9')
    return render(request,'promocion.html', {"promocion":promocion})

#Registro
def registroCliente(request):
    if request.method=='POST':
        nombre=request.POST['nombre']
        apellido=request.POST['apellido']
        correo= request.POST['correo']
        clave=request.POST['password']
        telefono=request.POST['telefono']
        fecha=request.POST['fecha']
        Cliente(nombre_cliente=nombre, apellido_cliente=apellido, correo_cliente=correo, clave_cliente=clave, telefono_cliente=telefono, fecharegistrocliente=fecha).save()
        messages.success(request, request.POST['nombre'] +' se registro correctamente.')
        return render(request, 'registrarse.html')
    else:
        return render(request, 'registrarse.html')

#Login
def paginaLogin(request):
    if request.method=='POST':
        try:
            detalleC=Cliente.objects.get(correo_cliente=request.POST['correo'], clave_cliente=request.POST['password'])
            print("Cliente=", detalleC)
            request.session['Email']=detalleC.correo_cliente
            return render(request, 'inicio.html')
        except Cliente.DoesNotExist as e:
            messages.success(request, 'Email o contraseña incorrecta!')
    return render(request, 'iniciarsesion.html')

def cerrarSesion(request):
    try:
        del request.session['Email']
        
    except:
        return render(request, 'inicio.html')
    return render(request, 'inicio.html')


#Delivery
def delivery(request):
    return render(request, 'delivery.html')

#Nosotros
def nosotros(request):
    return render(request, 'nosotros.html')


# Contacto
def contacto(request):
    formulario=FormularioContacto()
    
    if request.method=="POST":
        formulario=FormularioContacto(data=request.POST)
        if formulario.is_valid():
            nombre=request.POST.get("nombre")
            correo=request.POST.get("correo")
            mensaje=request.POST.get("mensaje")

            correo=EmailMessage("Mensaje desde Tragón Ball Z",
            "El usuario con nombre {} y correo {}  envia lo siguiente:\n\n {}".format(nombre,correo,mensaje),
            "",["tragonballzpyme@gmail.com"],reply_to=[correo])

            try: 
                correo.send()
                messages.success(request, 'Se ha enviado correctamente su mensaje.')
                return redirect("TragonBall:contacto")
            except:    
                return redirect("TragonBall:contacto")
    return render(request, "contacto.html", {"miFormulario":formulario})

#Tipos de pago
def tiposPago(request):
    return render(request, 'tiposPago.html')

def carro(request):
    return render(request, "carro.html")

def comprar(request):
    return render(request, "paypal/comprar.html")

