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

def insertarDepartamento(request):
    if ('cajaid' in request.POST):
        servicio = ServiceDepartamentos()
        id = request.POST['cajaid']
        nombre = request.POST['cajanombre']
        localidad = request.POST['cajalocalidad']
        servicio.insertarDepartamento(id, nombre, localidad)
        departamentos = servicio.getDepartamentos()
        context = {
            "departamentos": departamentos
        }
        return render(request, 'pages/index.html', context)
    else:
        return render(request, 'pages/create.html')
