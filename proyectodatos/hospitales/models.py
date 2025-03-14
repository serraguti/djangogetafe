from django.db import models
import oracledb

# Create your models here.
class Hospital:
    idHospital = 0
    nombre = ""
    direccion = ""
    telefono = ""
    camas = 0

class ServiceHospital:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM'
           , password='oracle', dsn='localhost/xe')
    
    def getHospitales(self):
        sql = "select * from HOSPITAL"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista = []
        for row in cursor:
            hosp = Hospital()
            hosp.idHospital = row[0]
            hosp.nombre = row[1]
            hosp.direccion = row[2]
            hosp.telefono = row[3]
            hosp.camas = row[4]
            lista.append(hosp)
        cursor.close()
        return lista

class Departamento:
    numero = 0
    nombre = ""
    localidad = ""

class ServiceDepartamentos:
    def __init__(self):
        self.connection = oracledb.connect(user='SYSTEM'
           , password='oracle', dsn='localhost/xe')
    
    def detallesDepartamento(self, numero):
        sql = "select * from DEPT where DEPT_NO=:p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero,))
        row = cursor.fetchone()
        dept = Departamento()
        dept.numero = row[0]
        dept.nombre = row[1]
        dept.localidad = row[2]
        cursor.close()
        return dept

    def updateDepartamento(self, numero, nombre, localidad):
        sql = "update DEPT set DNOMBRE=:p1, LOC=:p2 where DEPT_NO=:p3"
        cursor = self.connection.cursor()
        cursor.execute(sql, (nombre, localidad, numero))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros

    def eliminarDepartamento(self, numero):
        sql = "delete from DEPT where DEPT_NO=:p1"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero, ))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros

    def insertDepartamento(self, numero, nombre, localidad):
        sql = "insert into DEPT values (:p1, :p2, :p3)"
        cursor = self.connection.cursor()
        cursor.execute(sql, (numero, nombre, localidad))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros

    def getDepartamentos(self):
        sql = "select * from DEPT"
        cursor = self.connection.cursor()
        cursor.execute(sql)
        lista = []
        for row in cursor:
            dept = Departamento()
            dept.numero = row[0]
            dept.nombre = row[1]
            dept.localidad = row[2]
            lista.append(dept)
        cursor.close()
        return lista