from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# def saludar(request):
#     saludo = "Hola que tal"
#     respuesta_http = HttpResponse(saludo)
#     return respuesta_http

# def saludo_con_fecha(request):
#     hoy = datetime.now()
#     saludo = f"Hola, hoy es {hoy.day}/{hoy.month}/{hoy.year}"
#     respuesta_http = HttpResponse(saludo)
#     return respuesta_http

def html(request):
    contexto={}
    http_response = render(
        request=request,
        template_name='base.html',
        context=contexto
    )
    return http_response