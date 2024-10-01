""" #sumar
def sumar(a, b):
    return a + b
# restar
def restar(a, b):
    return a - b
# multiplicar
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: No se puede dividir por 0"
def calculadora():
    print("Calculadora básica")
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    
    
    opcion = int(input("Elige una operación (1-2-3-4): "))

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == 1:
        resultado = sumar(a, b)
    elif opcion == 2:
        resultado = restar(a, b)
    elif opcion == 3:
        resultado = multiplicar(a, b)
    elif opcion == 4:
        resultado = dividir(a, b)
    else:
        resultado = "Opción no válida"
    print("El resultado es:", resultado)

calculadora() """

""" def numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("No ingresaste un numero, intenta nuevamente")
            
numero1 = numero("Escribe el primer numero: ")
numero2 = numero("Escribe el segundo numero: ")

print("Suma: ", numero1 + numero2)
print("Resta: ", numero1  - numero2)
print("Multiplicacion: ", numero1 * numero2)
try:
    print("Division: ", numero1 /numero2)
except ZeroDivisionError:
    print("Division: No se puede dividir por cero") """
    
paises = {
    "ar":"Argentina",
    "cl": "Chile",
    "co": "Colombia",
    "uy": "Uruguay"
}
""" 
#'salir' sale del bucle
#codigo correcto, muestra el pais
#codigo incorrecto muestra un error (EXCEPT)



while True:
    print('1.- ar:Argentina\n2.- cl: Chile\n3.- co:Colombia\n4.- uy: Uruguay')
    codigo = input("Ingrese el codigo del país: ")
    if codigo == "salir":
        break
    try:
        print(paises[codigo])
    except KeyError:
        print("El codigo es invalido")
     """
""" 
def sumar(a,b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Se requieren dos numeros")
    return a + b

numero1 = int(input("Escribe el primer numero:  "))
numero2 = int(input("Escribe el segundo numero: "))

suma = sumar(2,2.0)
print(suma)

 """
 
""" frase_con_blanqueo = "No hay mal que ____ cien años"
palabra_correcta = "dure"

def adivinar_palabra(frase_con_blanqueo, palabra_correcta):
    print("***Adivina la palabra: "+ frase_con_blanqueo+"***")
    while True:
        entrada_usuario = input("Ingrese la palabra que falta: ").strip()
        
        if not isinstance(entrada_usuario, str) or entrada_usuario.isnumeric() == True:
            print("Entrada invalida. Por favor, ingresa una palabra valida")
            continue
        
        frase_con_entrada = frase_con_blanqueo.replace("____", entrada_usuario)
        if frase_con_entrada.find(palabra_correcta) != -1:
            print("¡Correcto! Has adivinado la palabra")
            return True
        else:
            print(f"Incorrecto, la palabra correcta era {palabra_correcta}")
            return False
        
adivinar_palabra(frase_con_blanqueo, palabra_correcta) """

""" texto = "Python"
texto2 = "Programming" """
#print(texto[0:6])
""" 
for letra in texto:
    print(letra) 
"""
""" lista = ["d","u","r","e"] 
texto = "dure"

print(lista[3])
print(texto[3])

lista[3] ="o"
texto[3] ="o"
print(lista)
print(texto)
#print(texto*3) """
""" texto = repr("\tomate\nuez")
print(texto) """

""" frase = "Python Programming"
print(frase.startswith("Programming"))
print(frase.endswith("Python"))

nombre = " Pedro "
print(nombre.strip()) 
texto = "\tomateuez\n"
print(texto)
"""

""" frase = "Hola mundo desde Python"
print(frase)
nueva_frase = frase.replace("Python", "JavaScript")
print(nueva_frase)

nombres = "Pedro Diego Lucia"
nombres_separados = nombres.split()
print(nombres_separados)
"""
 
""" cadena = "No hay mal que dure cien años"
print(cadena.find("tenga")) """

texto = "PABLITO CLAVO UN CLAVITO, que clavito clavo pablito"
""" print(texto.count("clavito"))
print(texto.upper())
print(texto.lower())
print(texto.capitalize())
print(texto.title())
print(texto.swapcase())
 """
 
dato = input("ingrese un dato: ")
while dato != "salir":
    if dato.isdecimal() == False:
        print("Es un texto")
    else:
        print("Es un numero")
    dato = input("ingrese un dato: ")