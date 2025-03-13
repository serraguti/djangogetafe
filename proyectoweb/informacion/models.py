from django.db import models
#import oracledb
import pyodbc
# Create your models here.

class Departamento: 
    numero = 0
    nombre = ""
    localidad = ""

class ServiceDepartamentos:
    def __init__(self):
        self.connection = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost\\DESARROLLO;DATABASE=HOSPITAL;UID=SA;TrustServerCertificate=yes') 

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

    def insertarDepartamento(self, numero, nombre, localidad):
        #sql = "insert into DEPT values (:id, :nombre, :localidad)"
        sql = "insert into DEPT values (?, ?, ?)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero, nombre, localidad))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros