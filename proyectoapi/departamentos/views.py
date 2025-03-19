from django.shortcuts import render
from departamentos.models import ServiceDepartamentos

# Create your views here.
def index(request):
    servicio = ServiceDepartamentos()
    departamentos = servicio.getDepartamentos()
    context = {
        "departamentos": departamentos
    }
    return render(request, 'pages/index.html', context)
