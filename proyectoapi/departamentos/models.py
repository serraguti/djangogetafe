from django.db import models
import requests

# Create your models here.
class Departamento:
    numero = 0
    nombre = ""
    localidad = ""

class ServiceDepartamentos:
    def __init__(self):
        self.url = "https://apiejemplos.azurewebsites.net/"

    def getDepartamentos(self):
        peticion = "api/departamentos"
        response = requests.get(self.url + peticion)
        json = response.json()
        lista = []
        for dato in json:
            dept = Departamento()
            dept.numero = dato["idDepartamento"]
            dept.nombre = dato["nombre"]
            dept.localidad = dato["localidad"]
            lista.append(dept)
        return lista
    
    def insertarDepartamento(self, numero, nombre, localidad):
        peticion = "api/departamentos"
        departamento = {
                        "idDepartamento": numero,
                        "nombre": nombre,
                        "localidad": localidad
                        }
        requests.post(self.url + peticion, json=departamento)
    
    def delete(self, numero):
        peticion = "api/departamentos/" + numero
        requests.delete(self.url + peticion)
        