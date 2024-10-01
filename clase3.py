'''
1.- Crear dos listas
2.- En un diccionario contabilziar las repeticiones
3.- mostrar el resultado
'''
""" 
lista1 =["Ana", "Luis", "Pedro", "Ana", "Juan"]
lista2 =["Pedro", "Luis", "Maria", "Pedro", "Marta"]

contador_nombres = {}

for nombre in lista1 + lista2:
    if nombre in contador_nombres:
        contador_nombres[nombre] += 1
    else:
        contador_nombres[nombre] = 1

print(contador_nombres)
lista_resultados = [contador_nombres]
print(lista_resultados) """
""" 
lista1 = ["manzana", "pera", "uva", "manzana", "banana"]
lista2 = ["banana", "manzana", "pera", "pera", "sandía"]

listas_unificadas = lista1 + lista2
contador = {}
#Contabilizar las repeticiones de cada fruta'''
for fruta in listas_unificadas:
    if fruta in contador:
        contador[fruta] += 1
    else:
        contador[fruta] = 1

print("Repeticiones de frutas", contador) """

""" def cuadrado(x):
    return x * x

numeros = [1, 2, 3, 4, 5]

#funcion de orden superior
def funcion_superior(funcion, lista):
    resultados = [] #guardamos los resultados
    
    for numero in lista:
        resultado = funcion(numero)
        resultados.append(resultado)
        
    return resultados

numeros_cuadrado = funcion_superior(cuadrado, numeros)

print(f"Numeros originales: {numeros} ")
print(f"Numeros elevados al cuadrado: {numeros_cuadrado}") """

'''
1.- Crear dos funciones, una para calcular iva y otra para calcular un descuento
2.- Crear una lista con precios
3.- Crear una funcion de orden superior que reciba cualquiera de las funciones y la lista
4.- Mostrar en consola la lista con la funcion aplicada
'''


#Funciones anónimas o funciones lambda

""" raiz_cuadrada = lambda x: x**2
print(raiz_cuadrada(5))

def superior(funcion, lista):
    resultado =[]
    for n in lista:
        resultado.append(funcion(n))
    return resultado

numeros = [2,5,10]

print(superior(lambda x: x**2, numeros))
print(superior(lambda x: x+100, numeros)) """



""" try:
    numero = input("Ingrese el numero a convertir a entero: ")
    print("Numero a convertir: "+ numero)
    print(type(numero))
    numero_entero = int(numero)
    print(f"Numero convertido:  {numero_entero}")
    print(type(numero_entero))
except ValueError:
    print("El dato no es un numero")
    
print("El programa sigue...") """
""" 
try:
    lista = [1,2,3]
    lista_enteros = int(lista)
    print(lista_enteros)
except TypeError:
    print("No se puede convertir una coleccion a entero")
     """

""" try:
    lista = [1,2,3]
    lista_enteros = int(lista)
    print(lista_enteros)
except (TypeError, ValueError):
    print("Ocurrio un error") """
    
""" try:
    lista = "Hola"
    lista_enteros = int(lista)
    print(lista_enteros)
except TypeError:
    print("No se puede convertir una coleccion a entero")
except ValueError:
    print("El dato no es un numero") """
    
""" try:
    tupla = "cadena"
    tupla_enteros = int(tupla)
    print(tupla_enteros)
except Exception:
    print("Ocurrio un error") """
    
""" try:
    numero = input("Ingrese el numero a convertir a entero: ")
    numero_int = int(numero)
    print(numero_int)
except Exception:
    print("Ocurrio un error")
else:
    print("La conversion se realizo correctamente") """
    

""" try:
    numero = input("Ingrese el numero a convertir a entero: ")
    numero_int = int(numero)
    print(numero_int)
except Exception:
    print("Ocurrio un error")
else:
    print("La conversion se realizo correctamente")
finally:
    print("Fin de la ejecucion de conversion") """
"""     
    
try:
    diccionario = {"nombre": "Cesar"}
    print(diccionario["edad"])
except KeyError:
    print("No se encontro la clave") """
    
""" try:
    lista = [10,20,30]
    print(lista[3])
except IndexError:
    print("No se encontro el indice") """

""" try:
    division = 10/0
    print(division)
except ZeroDivisionError:
    print("No se puede dividir el numero por cero") """
    
def obtener_numero(prompt):
    while True:
        try:
            numero = float(input(prompt))
            return numero
        except ValueError:
            print("El niumero ingresado no es valido, intenta nuevamente")


def dividir_numeros(dividendo, divisor):
    try:
        resultado = dividendo/divisor
        return resultado
    except ZeroDivisionError:
        print("Error, no puedes dividir un numero por cero")
        return None
    
numero_uno = obtener_numero("Ingresa el dividendo: ")
numero_dos = obtener_numero("Ingresa el divisor: ")

resultado = dividir_numeros(numero_uno, numero_dos)

if resultado is not None:
    print(f"El resultado de {numero_uno} dividido por {numero_dos} es {resultado}")