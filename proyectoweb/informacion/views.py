from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'informacion/index.html')

def pelis(request):
    return render(request, 'informacion/pelis.html')

def futbol(request):
    nombre = "Real Madrid"
    data = {
        "equipo": nombre
    }
    return render(request, 'informacion/futbol.html', data)

def jugadores(request):
    listaJugadores=[
        {
            "Nombre":"Cristiano Ronaldo",
            "Demarcacion":"Delantero",
            "Numero": 7
        },
        {
            "Nombre": "Guti",
            "Demarcacion": "Centrocampista",
            "Numero": 14
        },
        {
            "Nombre": "Karim Benzema",
            "Demarcacion": "Delantero",
            "Numero":9
        },
        {
            "Nombre": "Toni Kroos",
            "Demarcacion": "Centrocampista",
            "Numero":8
        },
        {
            "Nombre": "Thibaut Courtois",
            "Demarcacion": "Portero",
            "Numero": 1
        }
    ]

    context = {
        "jugadores": listaJugadores
    }
    return render(request, 'informacion/jugadores.html',context)

def colores(request):
    #RECUPERAMOS LA VARIABLE QUE NOS ESTAN ENVIANDO
    #MEDIANTE GET (micolor)
    #DEBEMOS COMPROBAR QUE RECIBIMOS ALGO LLAMADO micolor
    if ('micolor' in request.GET):
        colorRecibido = request.GET['micolor']
        #CON EL COLOR RECIBIDO SE LO DEVOLVEMOS AL DIBUJO
        #PARA PINTARLO
        context = {
            "colordibujo": colorRecibido
        }
        return render(request, 'informacion/colores.html',context)
    else:
        return render(request, 'informacion/colores.html')

def saludo(request):
    return render(request, 'informacion/saludo.html')