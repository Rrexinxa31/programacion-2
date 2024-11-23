import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def potencia(a, b):
    return a ** b

def porcentaje(a, b):
    return (a * b) / 100

def raiz(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Raíz negativa"

def mostrar_menu():
    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Porcentaje")
    print("7. Raíz cuadrada")
    print("8. Salir")

def seleccionar_operacion():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la operación que desea realizar: ")
        
        if opcion == "8":
            print("¡Hasta luego!")
            break
        
        if opcion in ["1", "2", "3", "4", "5", "6"]:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            if opcion == "1":
                print("Resultado:", sumar(a, b))
            elif opcion == "2":
                print("Resultado:", restar(a, b))
            elif opcion == "3":
                print("Resultado:", multiplicar(a, b))
            elif opcion == "4":
                print("Resultado:", dividir(a, b))
            elif opcion == "5":
                print("Resultado:", potencia(a, b))
            elif opcion == "6":
                print("Resultado:", porcentaje(a, b))
        elif opcion == "7":
            a = float(input("Ingrese un número: "))
            print("Resultado:", raiz(a))
        else:
            print("Opción no válida, por favor intente de nuevo.")

# Ejecución del programa
seleccionar_operacion()
