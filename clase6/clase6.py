""" import time

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

def ingreso_float(mensaje, error):
    dato = input(mensaje)
    while True:
        try:
            dato = float(dato)
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

def calcular(precios, pedido):
    total = 0
    total += pedido["comboSimple"] * precios["comboSimple"]
    total += pedido["comboDoble"] * precios["comboDoble"]
    total += pedido["comboTriple"] * precios["comboTriple"]
    total += pedido["mcFlurby"] * precios["mcFlurby"]
    return total
    
def confirmar():
    respuesta = ingreso_str("¿Confirma el pedido? Y/N", "Error, campo vacio")
    while respuesta.lower() not in ["y", "n", "yes", "no"]:
        print("Ingrese unicamente Y o N")
        respuesta = ingreso_str("¿Confirma el pedido? Y/N", "Error, campo vacio")
    return respuesta.lower() in ["y", "yes"]
    
def guardarVentas(data):
    renglon = ""
    for n in data:
        if n == "total":
            renglon += str(data[n]) + "\n"
        else:
            renglon += str(data[n]) + ","
    f = open("ventas.txt", "a")
    f.write(renglon)
    f.close()

def guardarEncargado(data):
    ingreso = "IN " + data["ingreso"] + " Encargado " + data["nombre"] +"\n"
    egreso = "OUT " +  data["egreso"] + " Encargado " + data["nombre"] + "$" + str(data["facturado"]) + "\n"
    separador = ("#"*50) + "\n"
    f = open("registro.txt", "a")
    f.write(ingreso)
    f.write(egreso)
    f.write(separador)
    f.close()


precios = {
    "comboSimple": 5,
    "comboDoble": 6,
    "comboTriple": 7,
    "mcFlurby": 2
}

salir = True

while salir:
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
            costoTotal = calcular(precios, pedido)
            print(f"Total ${costoTotal}")
            recibido = ingreso_float("Abona con $ ","Error, solo numeros")
            while costoTotal > recibido:
                print("Ingrese un monto mayor, no alcanza")
                recibido = ingreso_float("Abona con $ ","Error, solo numeros")
            print(f"Vuelto ${recibido - costoTotal}")
            estado = confirmar()
            if estado:
                caja += costoTotal
                pedido["fecha"] = time.asctime()
                pedido["total"] = costoTotal
                guardarVentas(pedido)
            else:
                print("Pedido cancelado")
        elif opcion == "2":
            datosEncargado["egreso"] = time.asctime()
            datosEncargado["facturado"] = caja
            guardarEncargado(datosEncargado)
            break
        elif opcion == "3":
            datosEncargado["egreso"] = time.asctime()
            datosEncargado["facturado"] = caja
            guardarEncargado(datosEncargado)
            print("¡Muchas gracias por usar el programa!")
            salir = False
            break
        else:
            print("Opcion incorrecta, vuelva a intentarlo")
            print("\n*3") """

""" import mi_modulo
mi_modulo.mi_funcion()

from mi_modulo import otra_funcion
otra_funcion() """

""" from mi_modulo import *
mi_funcion()
otra_funcion() """

'''
1.- Crear en un modulo, 3 funciones para calcular el area, cuadrado, circulo, rectangulo
#cuadrado lado ** 2
#circulo pi * r**2
#rectangulo base por altura
2.- Crear un funcion que me muestre el menu
3.- Crear una funcion main() que ejecute el programa
'''
""" 
import calculadora_areas

print(f"El area del cuadrado es: {calculadora_areas.area_cuadrado(2)}") """


class MiClase:
    def __init__(self, numero):
        self.a = numero
    
mi_objeto = MiClase(1)
otro_objeto = MiClase(5)

print(mi_objeto.a)
print(otro_objeto.a)