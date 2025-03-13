from django.shortcuts import render
from informacion.models import ServiceDepartamentos
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
    #PREGUNTAMOS DE FORMA OBLIGATORIA SI HEMOS
    #RECIBIDO DATOS DEL FORMULARIO
    if ('cajanombre' in request.POST):
        nombreRecibido = request.POST['cajanombre']
        context = {
            "nombre": nombreRecibido
        }
        return render(request, 'informacion/saludo.html', context)
    else:
        return render(request, 'informacion/saludo.html')
    
def sumarNumeros(request):
    if ('cajanumero1' in request.POST):
        num1 = request.POST['cajanumero1']
        num2 = request.POST['cajanumero2']
        suma = int(num1) + int(num2)
        context = {
            "suma": suma,
            "numero1": num1,
            "numero2": num2
        }
        return render(request, 'informacion/sumarnumeros.html',context)
    else:
        return render(request, 'informacion/sumarnumeros.html')

def collatz(request):
    if ('cajanumero' in request.POST):
        dato = request.POST['cajanumero']
        numero = int(dato)
        listanumeros = []
        while (numero != 1):
            if (numero % 2 == 0):
                numero = int(numero / 2)
            else:
                numero = int(numero * 3 + 1)
            listanumeros.append(numero)
        context = {
            "numeroscollatz": listanumeros
        }
        return render(request, 'informacion/collatz.html', context)
    else:
        return render(request, 'informacion/collatz.html')
    
def datos(request):
    servicio = ServiceDepartamentos()
    departamentos = servicio.getDepartamentos()
    context = {
        "departamentos": departamentos
    }
    return render(request, 'informacion/datos.html', context)

def tablaMultiplicar(request):
    if ('cajanumero' in request.POST):
        dato = request.POST["cajanumero"]
        numero = int(dato)
        listaTabla = []
        for i in range(10):
            resultado = numero * (i + 1) 
            operacion = str(numero) + " * " + str((i + 1))
            listaTabla.append({
                "operacion": operacion,
                "resultado": resultado
            })
        context = {
            "listatabla": listaTabla
        }
        return render(request, 'informacion/tabla.html', context)
    else:
        return render(request, 'informacion/tabla.html')
    
def insertarDepartamentos(request):
    #PREGUNTAMOS DE FORMA OBLIGATORIA SI HEMOS
    #RECIBIDO DATOS DEL FORMULARIO
    if ('cajanombre' in request.POST):
        nombre = request.POST['cajanombre']
        numero = request.POST['cajanumero']
        localidad = request.POST['cajalocalidad']
        servicio = ServiceDepartamentos();
        registros = servicio.insertarDepartamento(numero, nombre, localidad);
        context = {
            "insertados": registros
        }
        return render(request, 'informacion/insertar.html', context)
    else:
        return render(request, 'informacion/insertar.html')