def area_cuadrado(lado):
    return lado ** 2

def area_rectangulo(base, altura):
    return base * altura

def area_circulo(radio):
    from math import pi
    return pi * (radio ** 2)

def mostrar_menu():
    print("Calculadora de areas")
    print("1.- Area de un cuadrado")
    print("2.- Area de un rectangulo")
    print("3.- Area de un circulo")
    print("4.- Salir")
    
def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opcion deseada (1-4):")
        if opcion == "1":
            lado = float(input("Ingrese el lado del cuadrado: "))
            print(f"El area del cuadrado es: {area_cuadrado(lado)}")
        elif opcion == "2":
            base = float(input("Ingrese la base del rectangulo: "))
            altura = float(input("Ingrese la altura del rectangulo: "))
            print(f"El area del rectangulo es: {area_rectangulo(base, altura)}")
        elif opcion == "3":
            radio = float(input("Ingrese el radio del circulo: "))
            print(f"El area del circulo es: {area_circulo(radio)}")
        elif opcion == "4":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("La opcion ingresada no es valida, intente nuevemente")

#Ejecuta la funcion principal si este archivo se ejecuta directamente
#Documentacion: https://docs.python.org/3/library/__main__.html#
if __name__=="__main__":
    main()