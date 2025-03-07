from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'aplicacion/index.html')
    #return HttpResponse("Mi primera pagina Django!!!")

def metodoViernes(request):
    return HttpResponse("Hoy es viernes, mañana sábado")
