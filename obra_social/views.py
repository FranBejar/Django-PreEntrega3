from django.shortcuts import render, redirect
from django.urls import reverse

from obra_social.forms import AfiliacionFormulario
from obra_social.models import Afiliado,Especialista,Hospital

# Create your views here.

def lista_planes(request):
    contexto={}
    http_response = render(
        request=request,
        template_name='obra_social/planes.html',
        context=contexto
    )
    return http_response

def bienvenido(request):
    contexto={}
    http_response = render(
        request=request,
        template_name='obra_social/bienvenido.html',
        context=contexto
    )
    return http_response

def lista_medicos(request):
    contexto = {
        "medicos": Especialista.objects.all()
    }
    http_response = render(
        request=request,
        template_name='obra_social/cartilla.html',
        context=contexto
    )
    return http_response

def lista_hospitales(request):
    contexto = {
        "hospitales": Hospital.objects.all()
    }
    http_response = render(
        request=request,
        template_name='obra_social/hospitales.html',
        context=contexto
    )
    return http_response

def nuevo_afiliado(request):
    if request.method == "POST":
        formulario = AfiliacionFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            afiliado = Afiliado(
                nombre=data['nombre'],
                apellido=data['apellido'],
                dni=data['dni'],
                telefono=data['telefono'],
                email=data['email'],
                fecha_de_nacimiento=data['fecha_de_nacimiento'],
                direccion=data['direccion'],
                plan=data['plan']
            )
            afiliado.save()
            url_exitosa = reverse('bienvenido')
            return redirect(url_exitosa)
    else:
        formulario = AfiliacionFormulario()

    http_response = render(
        request=request,
        template_name='obra_social/afiliarse.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_medico(request):
    busqueda = request.POST.get("busqueda", "")
    
    if busqueda:
        medicos = Especialista.objects.filter(especialidad__contains=busqueda)
    else:
        medicos = Especialista.objects.all()

    contexto = {
        "medicos": medicos,
        "busqueda_form": busqueda,
    }

    return render(
        request=request,
        template_name='obra_social/cartilla.html',
        context=contexto
    )

