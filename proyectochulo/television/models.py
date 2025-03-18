from django.db import models
import oracledb

# Create your models here.
class Personaje:
    idPersonaje = 0
    nombre = ""
    imagen = ""
    idSerie = 0

class Serie:
    idSerie = 0
    titulo = ""
    imagen = ""
    year = 0

class ServiceSeries:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM'
                                           , password='oracle'
                                           , dsn='localhost/xe')
    
    def findPersonaje(self, idPersonaje):
        sql = "select * from PERSONAJES where IDPERSONAJE=:p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (idPersonaje, ))
        row = cursor.fetchone()
        person = Personaje()
        person.idPersonaje = row[0]
        person.nombre = row[1]
        person.imagen = row[2]
        person.idSerie = row[3]
        cursor.close()
        return person

    def updatePersonaje(self, idPersonaje, nombre, imagen, idSerie):
        sql = """
                update PERSONAJES set PERSONAJE=:p1
                , IMAGEN=:p2, IDSERIE=:p3 
                 where IDPERSONAJE=:p4
                """    
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, imagen, idSerie, idPersonaje))
        self.connection.commit()
        cursor.close()

    def getPersonajesSerie(self, idserie):
        sql = "select * from PERSONAJES where IDSERIE=:p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (idserie, ))
        lista = []
        for row in cursor:
            person = Personaje()
            person.idPersonaje = row[0]
            person.nombre = row[1]
            person.imagen = row[2]
            person.idSerie = row[3]
            lista.append(person)
        cursor.close()
        return lista

    def getPersonajes(self):
        sql = "select * from PERSONAJES"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista = []
        for row in cursor:
            person = Personaje()
            person.idPersonaje = row[0]
            person.nombre = row[1]
            person.imagen = row[2]
            person.idSerie = row[3]
            lista.append(person)
        cursor.close()
        return lista

    def getSeries(self):
        sql = "select * from SERIES"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista = []
        for row in cursor:
            serie = Serie()
            serie.idSerie = row[0]
            serie.titulo = row[1]
            serie.imagen = row[2]
            serie.year = row[3]
            lista.append(serie)
        cursor.close()
        return lista