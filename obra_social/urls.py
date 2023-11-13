from django.urls import path

from obra_social.views import lista_planes,lista_medicos, lista_hospitales,nuevo_afiliado,bienvenido,buscar_medico

urlpatterns = [
    path("planes/",lista_planes, name="planes"),
    path("cartilla/",lista_medicos, name="cartilla"),
    path("hospitales/",lista_hospitales, name="hospitales"),
    path("bienvenido/",bienvenido, name="bienvenido"),
    path("afiliate/",nuevo_afiliado, name="afiliate"),
    path("especialista/",buscar_medico, name="especialista")
]