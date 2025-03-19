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
    
def eliminar(request):
    servicio = ServiceDepartamentos()
    id = request.GET['id']
    servicio.delete(id)
    departamentos = servicio.getDepartamentos()
    context = {
        "departamentos": departamentos
    }
    return render(request, 'pages/index.html', context)

def modificar(request):
    servicio = ServiceDepartamentos()
    if ('cajaid' in request.POST):
        #UPDATE
        id = request.POST['cajaid']
        nombre = request.POST['cajanombre']
        localidad = request.POST['cajalocalidad']
        servicio.update(id, nombre, localidad)
        departamentos = servicio.getDepartamentos()
        context= {
            "departamentos":departamentos
        }
        return render(request, 'pages/index.html', context)
    elif ('id' in request.GET):
        #BUSCAR
        id = request.GET['id']
        dept = servicio.findDepartamento(id)
        context = {
            "departamento": dept
        }
        return render(request, 'pages/update.html', context)
    
