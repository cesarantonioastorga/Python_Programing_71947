""" datos = [1,2,3]
print(4 in datos)
print(3 not in datos)

alumnos = {"Diego":10}
print("Diego" in alumnos) """



""" if edad < 20:
    print("Tenes menos de 20")
    if edad < 10:
        print("Tenes menos de 10")
    else:
        print("Tenes entre 10 y 19")
else:
    print("Tenes 20 o más") """

""" edad = 12

if edad < 20:
    print("Tenes menos de 20")
elif edad >=20:
    print("Tenes 20 o más")
else:
    print("Ocurrio un error") """
    
""" a = 0
while True:
    if a < 10:
        a += 1
        if a == 5:
            continue
        print(a)
    else:
        break """
        
""" lista = ["pera", "manzana", "papaya"]

for fruta in lista:
    print(fruta)
lista = ["pera", "manzana", "papaya"]  
print(lista[:2])
 """ 
'''
Crear un bucle que almacene en una variable la suma
de todos los elemento de una lista, con excepción del útlimo
'''

""" lista = [1, 2, 3, 4, 5]
suma = 0
for i in range(len(lista) - 1):
    suma += lista[i]
print("La suma de todos los elementos menos el último es:", suma) """

""" print()#out
input()#input 
range(1,101,3)

int()
float()

lista = [1, 2, 3, 4, 5]
print(len(lista))
"""
""" 
def suma(a, b):
    print(a + b)
    
resultado = suma(2,4)
otro_resutado = resultado + 10 
print( suma(2,4))
"""
""" 
def mostrar_mensaje(b, mensaje="No se ha agregado un mensaje"):
    print(mensaje)
    print(b)
    
mostrar_mensaje(3,"Esto es un mensaje") """
'''
def sumar(a, b):
 
    Descripción de la funcion:
    Esta función retorna una suma
    
    return a + b

help(sumar)
'''

'''
Crear una funcion que reciba como argumento la cantidad de numeros fibonaccio a mostrar
Chequear que el argumento ingresado sea mayor a 2
'''
""" def fibonacci(cantidad):
    if cantidad <=2:
        return "La cantidad debe ser mayor a dos"
    fibo = [0,1]
    
    while len(fibo) < cantidad:
        fibo.append(fibo[-1]+fibo[-2])
    return fibo

lista = fibonacci(2) """


""" 
def sumar():
    global suma
    suma= 2 + 5
    print(suma)

sumar()
print(suma) """

""" def funcion(entrada):
    entrada = 0

dato = 5
funcion(dato)
print(dato) """

""" def sumar (a,b):
    return a + b

sumar(2,5,6) """

""" def sumar(numeros):
    parcial = 0
    for n in numeros:
        parcial += n
    return parcial
print(sumar([20,40,30])) """

""" def sumar(*args):
    print(type(args))
    print(args)
    total = 0
    for n in args:
        total += n
    return total
    
suma = sumar(20,30,40,80)
print(suma) """

""" def sumar(**kwargs):
    print(type(kwargs))
    print(kwargs)
    total = 0
    for n in kwargs:
        total += kwargs[n]
    return total

suma = sumar(a=5,b=3,c=8, d=4)
print(suma) """

def funcion(a,b,*args,c=50,**kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)