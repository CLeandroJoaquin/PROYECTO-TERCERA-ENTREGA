from django.shortcuts import render
from Personal.models import Operador, Supervisor, Gerente
# Create your views here.


def listar_operarios(request):
    contexto = {
        "Personal": Operador.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='carpeta_principal/lista_operarios.html',
        context=contexto,
    )
    return http_response

