

""" conexion = pymysql.connect(
    host="localhost",
    port=3306,
    user = "root",
    passwd = "",
    db="database"
)

cursor = conexion.cursor()
#cursor.execute("CREATE TABLE personas(nombre TEXT, edad NUMERIC)")

personas = (
    ("Pablo", 20),
    ("Luis", 30),
    ("Lucas", 40)
)

try:
    for nombre, edad in personas:
        cursor.execute("INSERT INTO personas VALUES (%s, %s)", (nombre, edad))
except pymysql.err.InternalError:
    print("La consulta no se realizo correctamente")

conexion.commit()
conexion.close() """

'''
pymysql.err.InternalError: 
Captura errores internos del servidor, como problemas con la ejecución de consultas que el servidor no puede manejar correctamente.

pymysql.err.ProgrammingError: 
Captura errores relacionados con la sintaxis SQL o problemas con el código SQL.

pymysql.err.OperationalError: 
Captura errores relacionados con la operación del servidor de base de datos, como pérdida de conexión, fallos en la conexión a la base de datos, etc.

pymysql.err.DatabaseError: 
Captura errores generales relacionados con la base de datos, incluidos InternalError, ProgrammingError, OperationalError, etc.
'''

""" import pymysql
from datetime import date

class Database:
    def __init__(self, host, user, password, db):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        
    def connect(self):
        return pymysql.connect(
            host = self.host,
            user = self.user,
            password= self.password,
            db = self.db
        )
    
    def create_table(self):
        connection = self.connect()
        try: 
            with connection.cursor() as cursor:
                cursor.execute("CREATE TABLE IF NOT EXISTS alumnos (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255) NOT NULL, apellido VARCHAR(255) NOT NULL, edad INT NOT NULL, curso VARCHAR(255) NOT NULL, fecha_registro DATE NOT NULL)")
                connection.commit()
                print("Tabla 'alumnos' se ha creado correctamente")
        finally:
            connection.close()
            
class Alumno:
    def __init__(self, nombre, apellido, edad, curso, fecha_registro):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.curso = curso
        self.fecha_registro = fecha_registro
        
    
    def guardar(self, cursor):
        sql = "INSERT INTO alumnos (nombre, apellido, edad, curso, fecha_registro) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql,(self.nombre, self.apellido, self.edad, self.curso, self.fecha_registro))
        cursor.connection.commit()
        
    def leer_todos(cursor):
        sql = "SELECT * FROM alumnos"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def actualizar(cursor, alumno_id, nombre, apellido, edad, curso, fecha_registro):
        sql = "UPDATE alumnos SET nombre=%s, apellido=%s, edad=%s, curso=%s, fecha_registro=%s WHERE id=%s"
        cursor.execute(sql, (nombre, apellido,  edad, curso, fecha_registro, alumno_id))
        cursor.connection.commit()
        
    def eliminar(cursor, alumno_id):
        sql = "DELETE FROM alumnos WHERE id=%s"
        cursor.execute(sql, (alumno_id))
        cursor.connection.commit()
        
class Menu:
    def mostrar(self):
        print("\n---Menu---")
        print("1.- Agregar alumno")
        print("2.- Leer alumnos")
        print("3.- Modificar alumno")
        print("4.- Eliminar alumno")
        print("5.- Salir")
        
    def agregar_alumno(self, cursor):
        nombre = input("Nombre del alumno: ")
        apellido = input("Apellido del alumno: ")
        edad = int(input("Edad del alumno: "))
        curso = input("Curso del alumno: ")
        fecha_registro = date.today()
        
        alumno = Alumno(nombre, apellido, edad, curso, fecha_registro)
        alumno.guardar(cursor)
        print("Alumno agregado con éxito")
        
    def leer_alumnos(self, cursor):
        alumnos = Alumno.leer_todos(cursor)
        for alumno in alumnos:
            print(alumno)
            
    def modificar_alumno(self, cursor):
        alumno_id = int(input("ID del alumno a modificar: "))
        nombre = input("Nuevo nombre del alumno: ")
        apellido = input("Nuevo apellido del alumno: ")
        edad = int(input("Nuevo edad del alumno: "))
        curso = input("Nuevo curso del alumno: ")
        fecha_registro = date.today()
        Alumno.actualizar(cursor, alumno_id, nombre, apellido, edad, curso, fecha_registro)
        print("Alumno se ha actualizado con éxito")
        
    def eliminar_alumno(self, cursor):
        alumno_id = int(input("ID del alumno a eliminar"))
        Alumno.eliminar(cursor, alumno_id)
        print("Alumno eliminado con éxito")

def main():
    db = Database(host="localhost", user="root", password="", db="database")
    db.create_table()
    
    try:
        connection = db.connect()
        with connection.cursor() as cursor:
            menu = Menu()
            while True:
                menu.mostrar()
                opcion = input("Selecciona una opcion: ")
                if opcion == "1":
                    menu.agregar_alumno(cursor)
                elif opcion == "2":
                    menu.leer_alumnos(cursor)
                elif opcion == "3":
                    menu.modificar_alumno(cursor)
                elif opcion == "4":
                    menu.eliminar_alumno(cursor)
                elif opcion == "5":
                    print("Hasta luego!")
                    break
                else:
                    print("La opcion ingresada no es válida")
    finally:
        if connection:
            connection.close()
            
if __name__=="__main__":
    main() """
    
import requests

#GET Leer
#POST Agregar
#PUT Modificar
#DELETE Borrar

""" r = requests.get("https://www.google.com")
print(r.status_code) """

""" r = requests.get("https://api.github.com/events")
print(r.json()) """
""" 
r = requests.get("http://localhost:7001/student")
print(r.status_code)
print(r.json()) """

""" r = requests.post("http://localhost:7001/student", json={"name":"Lautaro", "courses": 3})
print(r.status_code)
print(r.json()) 
 """
""" r = requests.get("http://localhost:7001/student")
if r.status_code == 200:
    respuesta = r.json()
    for alumno in respuesta["students"]:
        print("Id alumno: ", alumno["id"])
        print("Nombre: ", alumno["nombre"])
        print("Cursos: ", alumno["cursos"])
else:
    print("Ocurrio un error") """
    
""" datos = {"courses": 6}
r = requests.put("http://localhost:7001/student/0", json=datos)
print(r.status_code) """

r = requests.delete("http://localhost:7001/student/0")
print(r.status_code)