from django.shortcuts import render
from television.models import ServiceSeries

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def metodoSeries(request):
    servicio = ServiceSeries()
    series = servicio.getSeries()
    context = {
        "series": series
    }
    return render(request, 'pages/series.html', context)
