""" numero = 1
mensaje = "El numero es: "
frase_completa = "{0} {1}"
#print(mensaje,numero)
#print(mensaje + str(numero))
print(frase_completa.format(mensaje, numero))
print(f"Algo: {mensaje}{numero}")
print("%s %d"%(mensaje, numero)) """

#C:\\Users\\Cesar\\Desktop\\Python\\archivo.txt
#C:/Users/Cesar/Desktop/Python/archivo.txt



#Modificar el archivo
""" archivo = open("archivo.txt", "w")
archivo.write("Algo desde Python")
archivo.close() """

""" #Agregar al archivo
archivo = open("archivo.txt", "a")
archivo.write("\nOtro texto desde Python")
archivo.close()


#Leer el archivo
archivo = open("archivo.txt", "r")
#print(archivo.read())
print(archivo.readline())
print(archivo.readlines())
archivo.close() """

""" with open("archivo.txt", "a") as archivo:
    archivo.write("Texto con with")

#with open("archivo.txt", "w") as archivo:
#    archivo.write("Texto con with")

with open("archivo.txt", "r") as archivo:
    texto = archivo.read()
    print(texto) """
    
'''
Guardar los nombres en un archivo
#roberto-20
#romina-32
Nombres con minuscula y el nombre y la edad separado con un guion
Usar except FileNotFoundError y with
'''
""" personas = {"Juan": 20, "Romina": 32, "Tamara": 25, "Melanie": 19}
nombre_archivo = "nombres.txt"
try:
    with open(nombre_archivo, "w") as archivo:
        for nombre, edad in personas.items():
            archivo.write(f"{nombre.lower()}-{edad}\n")
    print(f"Se a guardado correctamente {nombre_archivo}.")
    
except FileNotFoundError:
    print(f"Error: No se pudo encontrar o crear el archivo {nombre_archivo}.") """
    

""" nombre_archivo = "nombres.txt"
try:
    with open(nombre_archivo, "r") as archivo:
        personas_recuperadas = {}
        for linea in archivo:
            linea = linea.strip()
            nombre, edad = linea.split("-")
            personas_recuperadas[nombre] = int(edad)
    print("Diccionario creado desde el archivo:")
    print(personas_recuperadas)
except FileNotFoundError:
    print(f"Error: No se pudo encontrar el archivo {nombre_archivo}.") """
    
""" import math #importo el modulo
print(math.sqrt(25))
print(math.pi)

from math import sqrt
print(sqrt(9))

from math import * #importo las funcionalidades
print(pi)

import tkinter as tk """

import time

#Funciones para verifcar datos ingresados
def ingreso_str(mensaje, error):
    dato = input(mensaje)
    while dato == "":
        print(error)
        dato = input(mensaje)
    return dato

def ingreso_int(mensaje, error):
    dato = input(mensaje)
    while True:
        try:
            dato = int(dato)
            break
        except ValueError:
            print(error)
        dato = input(mensaje)
    return dato

def saludar(nombre):
    print("Hamburguesas IT")
    print("Encargado>>"+nombre)
    print("Recuerda comenzar con una sonrisa :)")

def ingresar():
    print("Bienvenido a Hamburguesas IT")
    nombre = ingreso_str("Ingrese su nombre encargado: ", "Error, campo vacio")
    return nombre

precios = {
    "comboSimple": 5,
    "comboDoble": 6,
    "comboTriple": 7,
    "mcFlurby": 2
}

while True:
    datosEncargado = {
        "nombre":"",
        "ingreso":"",
        "egreso":"",
        "facturado": 0
    }
    encargado = ingresar()
    inicio = time.asctime()
    datosEncargado["nombre"] = encargado
    datosEncargado["ingreso"] = inicio
    caja = 0
    print("\n" * 2)
    while True:
        saludar(encargado)
        print("1.- Ingreso de nuevo pedido")
        print("2.- Cambio de turno")
        print("3.- Apagar el sistema")
        opcion = ingreso_str(">>>", "Error, ingreso vacio")
        if opcion == "1":
            print("\n" * 2)
            pedido = {
                "cliente":"",
                "fecha":"",
                "comboSimple":0,
                "comboDoble":0,
                "comboTriple":0,
                "mcFlurby": 0,
                "total": 0
            }
            pedido["cliente"] = ingreso_str("Ingrese el nombre del cliente: ", "Error. No dejes este campo vacio")
            pedido["comboSimple"] = ingreso_int("Ingrese la cantidad del combo simple: ", "Error. Solo ingresa numeros")
            pedido["comboDoble"] = ingreso_int("Ingrese la cantidad del combo doble: ", "Error. Solo ingresa numeros")
            pedido["comboTriple"] = ingreso_int("Ingrese la cantidad del combo triple: ", "Error. Solo ingresa numeros")
            pedido["mcFlurby"] = ingreso_int("Ingrese la cantidad de mcFlurby: ", "Error. Solo ingresa numeros")