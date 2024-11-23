from datetime import datetime

# Tarifas del parqueadero por fracción de 15 minutos
PRECIO_MOTO = 500
PRECIO_CARRO = 1000

# Listas y variables para almacenar los datos
vehiculos = []  # Lista de vehículos registrados
cantidad_motos = 0  # Contador de motos ingresadas
cantidad_carros = 0  # Contador de carros ingresados
dinero_total = 0  # Dinero total recaudado

# Función para calcular la duración en minutos entre la hora de entrada y salida
def calcular_duracion(hora_entrada, hora_salida):
    formato = "%H:%M"  # Definimos el formato de la hora (24 horas)
    entrada_dt = datetime.strptime(hora_entrada, formato)
    salida_dt = datetime.strptime(hora_salida, formato)
    duracion = int((salida_dt - entrada_dt).total_seconds() // 60)  # Duración en minutos
    return duracion

# Función para calcular el costo del parqueo en función de la duración
def calcular_cobro(duracion, tipo_vehiculo):
    fracciones = (duracion + 14) // 15  # Redondeamos al siguiente múltiplo de 15 minutos
    if tipo_vehiculo == "moto":
        return fracciones * PRECIO_MOTO
    elif tipo_vehiculo == "carro":
        return fracciones * PRECIO_CARRO

# Función para registrar la entrada de un vehículo
def registrar_entrada():
    global cantidad_motos, cantidad_carros
    tipo = input("¿Es un carro o una moto? (carro/moto): ").lower()
    placa = input("Ingrese la placa del vehículo: ").upper()
    hora_entrada = input("Ingrese la hora de entrada (formato 24 horas, ej. 10:35): ")
    
    # Añadir vehículo a la lista
    vehiculo = {
        "tipo": tipo,
        "placa": placa,
        "hora_entrada": hora_entrada,
        "hora_salida": None,
        "duracion": None,
        "precio": None
    }
    
    vehiculos.append(vehiculo)  # Guardamos los datos del vehículo

    # Incrementamos contadores de motos o carros
    if tipo == "moto":
        cantidad_motos += 1
    elif tipo == "carro":
        cantidad_carros += 1
    else:
        print("Tipo de vehículo no válido.")
    
    print(f"Vehículo registrado: {tipo} con placa {placa} a las {hora_entrada}.\n")

# Función para registrar la salida y calcular la duración y costo del parqueo
def registrar_salida():
    global dinero_total
    placa = input("Ingrese la placa del vehículo que va a salir: ").upper()
    vehiculo = next((v for v in vehiculos if v["placa"] == placa and v["hora_salida"] is None), None)
    
    if vehiculo:
        hora_salida = input("Ingrese la hora de salida (formato 24 horas, ej. 12:15): ")
        duracion = calcular_duracion(vehiculo["hora_entrada"], hora_salida)
        precio = calcular_cobro(duracion, vehiculo["tipo"])
        
        # Actualizamos los datos del vehículo
        vehiculo["hora_salida"] = hora_salida
        vehiculo["duracion"] = duracion
        vehiculo["precio"] = precio
        
        dinero_total += precio  # Añadimos el precio al total recaudado

        print(f"Vehículo {vehiculo['tipo']} con placa {placa} estuvo {duracion} minutos.")
        print(f"Total a pagar: ${precio}\n")
    else:
        print("Vehículo no encontrado o ya salió.\n")

# Función para mostrar el reporte del parqueadero
def mostrar_reporte():
    print("\n--- Reporte del Parqueadero ---")
    print(f"Cantidad de motos: {cantidad_motos}")
    print(f"Cantidad de carros: {cantidad_carros}")
    print(f"Dinero total recaudado: ${dinero_total}\n")

# Función que muestra el menú principal
def menu():
    while True:
        print("1. Registrar entrada de vehículo")
        print("2. Registrar salida de vehículo")
        print("3. Mostrar reporte del parqueadero")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_entrada()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            mostrar_reporte()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.\n")

# Ejecutamos el menú para comenzar el programa
menu()
