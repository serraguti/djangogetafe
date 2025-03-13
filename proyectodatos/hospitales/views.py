from django.shortcuts import render
from hospitales.models import ServiceDepartamentos

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def departamentosBBDD(request):
    servicio = ServiceDepartamentos()
    departamentos = servicio.getDepartamentos()
    context = {
        "departamentos": departamentos
    }
    return render(request, 'pages/departamentos.html', context)
