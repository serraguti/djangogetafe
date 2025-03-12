from django.db import models
import oracledb
# Create your models here.

class Departamento: 
    numero = 0
    nombre = ""
    localidad = ""

class ServiceDepartamentos:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM', password='oracle', dsn='localhost/xe')

    def getDepartamentos(self):
        sql = "select * from DEPT"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        departamentos = []
        for row in cursor:
            dept = Departamento()
            dept.numero = row[0]
            dept.nombre = row[1]
            dept.localidad = row[2]
            departamentos.append(dept)
        cursor.close()
        return departamentos