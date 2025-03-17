from django.db import models
import oracledb

# Create your models here.
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