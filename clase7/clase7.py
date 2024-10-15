""" class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def mostrar_nombre(self):
        print(self.nombre)
        
mi_objeto = MiClase("Juan")
otro_objeto = MiClase("Pedro")

mi_objeto.mostrar_nombre() """

""" class Clase:
    __atributo_clase = "Hola"
    
    def __metodo(self):
        print("Hola mundo")
    
objeto = Clase()
print(objeto.atributo_clase)
objeto.metodo() """

""" class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
        
    def getnombre(self):
        return self.__nombre
    
    def getsalario(self):
        return self.__salario
    
    def setnombre(self, nombre):
        self.__nombre = nombre
        
    def setsalario(self, salario):
        self.__salario = salario
        
    def delnombre(self):
        del self.__nombre
        
    def delsalario(self):
        del self.__salario """
        

""" class Empleado:
    def __init__(self, nombre, salario):
        self.__nombre = nombre
        self.__salario = salario
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @nombre.deleter
    def nombre(self):
        del self.__nombre
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, salario):
        self.__salario = salario
    
    @salario.deleter
    def salario(self):
        del self.__salario """
        
""" class ClassA:
    def __init__(self):
        self.a = 1

class ClassB(ClassA):
    pass """
    
""" class ClassA:
    def __init__(self):
        self.a = 1

class ClassB(ClassA):
    def __init__(self):
        super().__init__()
        self.b = 2

mi_objeto = ClassB()
print(mi_objeto.a)
print(mi_objeto.b) """


""" class Forma:
    def dibujar(self):
        return "Dibujando una forma cualquiera"
    
class Circulo():
    def dibujar(self):
        return "Dibujando un circulo"

class Cuadrado():
    def dibujar(self):
        return "Dibujando un cuadrado"
    
def mostrar_dibujo(forma):
    print(forma.dibujar())
    
mi_circulo = Circulo()
mi_cuadrado = Cuadrado()
mi_forma = Forma()

mostrar_dibujo(mi_circulo)
mostrar_dibujo(mi_cuadrado)
mostrar_dibujo(mi_forma) """

""" class ClassA:
    def __init__(self):
        self.a = 1
    
    def mensaje_a(self):
        print("Desde A")

class ClassB():
    def __init__(self):
        self.b = 2
    
    def mensaje_b(self):
        print("Desde B")
        
class ClassC(ClassB, ClassA):
    pass

mi_objeto = ClassC()
mi_objeto.mensaje_a()
mi_objeto.mensaje_b()
 """
 
#ejercicio

''' class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario  # Atributo privado

    def get_salario(self):
        """Método para obtener el salario."""
        return self.__salario

    def set_salario(self, valor):
        """Método para establecer el salario."""
        if valor < 0:
            raise ValueError("El salario no puede ser negativo.")
        self.__salario = valor

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario: {self.__salario}"


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)  # Llamada al constructor de la clase base
        self.__departamento = departamento  # Atributo privado adicional

    def get_departamento(self):
        """Método para obtener el departamento."""
        return self.__departamento

    def set_departamento(self, departamento):
        """Método para establecer el departamento."""
        self.__departamento = departamento

    def __str__(self):
        return f"Gerente: {self.nombre}, Salario: {self.get_salario()}, Departamento: {self.__departamento}"


def obtener_salario():
    """Solicita un salario al usuario y valida la entrada."""
    while True:
        try:
            salario = float(input("Introduce el salario del empleado/gerente: "))
            if salario < 0:
                raise ValueError("El salario no puede ser negativo.")
            return salario
        except ValueError as e:
            print(e)
            print("Por favor, ingresa un valor numérico positivo.")


def obtener_departamento():
    """Solicita el departamento del gerente al usuario."""
    return input("Introduce el departamento del gerente: ")


# Solicitar al usuario si quiere crear un Empleado o un Gerente
tipo = input("¿Deseas crear un (E)mpleado o un (G)erente? (E/G): ").strip().upper()

if tipo == 'E':
    # Crear una instancia de Empleado
    nombre = input("Introduce el nombre del empleado: ")
    salario = obtener_salario()
    empleado = Empleado(nombre, salario)
    print(empleado)

elif tipo == 'G':
    # Crear una instancia de Gerente
    nombre = input("Introduce el nombre del gerente: ")
    salario = obtener_salario()
    departamento = obtener_departamento()
    gerente = Gerente(nombre, salario, departamento)
    print(gerente)

else:
    print("Opción no válida. Por favor, elige 'E' para Empleado o 'G' para Gerente.")
'''

#import os

#print(os.listdir()) #Lista los elementos del directorio actual
#print(os.listdir("C:/Users/Cesar/Desktop/desk/bootcamps/E/Python Programing 6/Python avanzado 23-08-2024")) #Lista los elementos del directorio indicado
#print(os.getcwd()) #Muestra la ruta actual
#os.mkdir("nueva_carpeta") #crea una carpeta en la ruta actual
#os.mkdir("C:\\Users\\Cesar\\Desktop\\desk\\bootcamps\\E\\Python Programing 6\\Python avanzado 17-09-2024\\Clase 7\\practica\\nueva_carpeta\\otra_carpeta") #crea una carpeta en la ruta indicada
#print(os.path.exists("C:\\Users\\Cesar\\Desktop\\desk\\bootcamps\\E\\Python Programing 6\\Python avanzado 17-09-2024\\Clase 7\\practica\\nueva_carpeta\\otra_carpeta")) #Verifica si la ruta existe
#os.rename("nueva_carpeta", "carpeta_renombrada") #renombra archivos o carpetas
#os.remove("archivo.py") #borra archivos
#os.rmdir("carpeta_renombrada") #borra carpetas vacias
#os.system("cls") #Limpia la consola

#import shutil

#shutil.copy("clase7.py", "carpeta/copia_Clase7.py") #para copiar archivos
#shutil.move("carpeta/copia_Clase7.py", "otra_carpeta")
#shutil.rmtree("otra_carpeta")

import sqlite3

conexion = sqlite3.connect("database.db")
cursor = conexion.cursor()

#cursor.execute("CREATE TABLE personas(nombre TEXT, edad NUMERIC)")
""" 
personas = (
    ("Juan", 40),
    ("Pedro", 35),
    ("Luis", 25)
)
try:
    for nombre, edad in personas:
        cursor.execute("INSERT INTO personas VALUES (?,?)", (nombre, edad))
except sqlite3.OperationalError:
    print("La consulta no se ejecuto correctamente") """

'''
sqlite3.DatabaseError: 
Clase base para errores generales relacionados con la base de datos.

sqlite3.OperationalError: 
Errores operacionales como problemas con el archivo de la base de datos o bloqueos.

sqlite3.ProgrammingError: 
Errores de sintaxis o problemas con el código SQL.

sqlite3.IntegrityError: 
Violaciones de restricciones de integridad.

sqlite3.DataError: 
Problemas con datos no válidos.

sqlite3.InterfaceError: 
Errores relacionados con el uso de la interfaz de base de datos.
'''

#conexion.commit()

cursor.execute("SELECT * FROM personas")
personas = cursor.fetchall()
print(personas)
conexion.close()