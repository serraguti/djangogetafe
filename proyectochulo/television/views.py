from django.shortcuts import render
from television.models import ServiceSeries

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

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
