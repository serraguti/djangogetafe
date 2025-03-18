from django.shortcuts import render
from television.models import ServiceSeries

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def personajesSeries(request):
    #PREGUNTAMOS SI HEMOS RECIBIDO EL DATO DE idserie EN GET
    if ('idserie' in request.GET):
        servicio = ServiceSeries()
        idserie = request.GET['idserie']
        personajes = servicio.getPersonajesSerie(idserie)
        context = {
            "personajes": personajes
        }
        return render(request, 'pages/personajesserie.html', context)
    else:
        return render(request, 'pages/personajesserie.html')

def modificarPersonaje(request):
    if ('idpersonaje' in request.GET):
        return render(request, 'pages/modificarpersonaje.html')
    else:
        return render(request, 'pages/modificarpersonaje.html')

def metodoPersonajes(request):
    servicio = ServiceSeries()
    personajes = servicio.getPersonajes()
    context = {
        "personajes": personajes
    }
    return render(request, 'pages/personajes.html', context)

def metodoSeries(request):
    servicio = ServiceSeries()
    series = servicio.getSeries()
    context = {
        "series": series
    }
    return render(request, 'pages/series.html', context)
