from datetime import datetime

# Constantes
PRECIO_MOTO = 500    # Precio por fracción de 15 minutos para motos
PRECIO_CARRO = 1000  # Precio por fracción de 15 minutos para carros

# Variables para contar vehículos y dinero recolectado
motos_ingresadas = 0
carros_ingresados = 0
dinero_total = 0

# Diccionario para almacenar los vehículos en el parqueadero
vehiculos = {}

# Función para registrar el ingreso de un vehículo
def registrar_ingreso():
    global motos_ingresadas, carros_ingresados
    tipo = input("¿El vehículo es MOTO o CARRO? ").strip().lower()
    
    if tipo not in ["moto", "carro"]:
        print("Tipo de vehículo no válido. Intente nuevamente.")
        return
    
    placa = input("Ingrese la placa del vehículo: ").strip().upper()
    
    if placa in vehiculos:
        print("Este vehículo ya está registrado.")
        return
    
    hora_entrada = input("Ingrese la hora de entrada (formato 24 horas: HH:MM): ")
    
    try:
        hora_entrada = datetime.strptime(hora_entrada, "%H:%M")
    except ValueError:
        print("Hora no válida. Asegúrese de ingresar en el formato correcto.")
        return
    
    # Almacenar la información del vehículo
    vehiculos[placa] = {
        "tipo": tipo,
        "hora_entrada": hora_entrada
    }
    
    if tipo == "moto":
        motos_ingresadas += 1
    elif tipo == "carro":
        carros_ingresados += 1
    
    print(f"Vehículo {tipo.upper()} con placa {placa} registrado exitosamente.")

# Función para registrar la salida de un vehículo y calcular el precio a pagar
def registrar_salida():
    global dinero_total
    placa = input("Ingrese la placa del vehículo que va a salir: ").strip().upper()
    
    if placa not in vehiculos:
        print("Este vehículo no está registrado.")
        return
    
    hora_salida = input("Ingrese la hora de salida (formato 24 horas: HH:MM): ")
    
    try:
        hora_salida = datetime.strptime(hora_salida, "%H:%M")
    except ValueError:
        print("Hora no válida. Asegúrese de ingresar en el formato correcto.")
        return
    
    vehiculo = vehiculos[placa]
    hora_entrada = vehiculo["hora_entrada"]
    
    # Calcular la duración en minutos
    duracion = (hora_salida - hora_entrada).total_seconds() // 60  # Duración en minutos
    fracciones_15_min = (duracion + 14) // 15  # Se redondea hacia arriba cada 15 min
    
    # Calcular el costo
    if vehiculo["tipo"] == "moto":
        costo = fracciones_15_min * PRECIO_MOTO
    elif vehiculo["tipo"] == "carro":
        costo = fracciones_15_min * PRECIO_CARRO
    
    # Sumar al total de dinero recolectado
    dinero_total += costo
    
    # Eliminar el vehículo del registro
    del vehiculos[placa]
    
    print(f"Duración del parqueo: {duracion} minutos")
    print(f"Total a pagar: ${costo}")
    print("Gracias por su visita.")

# Función para mostrar el estado del parqueadero (estadísticas)
def mostrar_estadisticas():
    print(f"\nEstadísticas del parqueadero:")
    print(f"Total de motos ingresadas: {motos_ingresadas}")
    print(f"Total de carros ingresados: {carros_ingresados}")
    print(f"Dinero recolectado: ${dinero_total}\n")

# Función principal del menú
def menu():
    while True:
        print("\n--- Menú del Parqueadero ---")
        print("1. Registrar ingreso de vehículo")
        print("2. Registrar salida de vehículo")
        print("3. Mostrar estadísticas del parqueadero")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            registrar_ingreso()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            print("Gracias por usar el sistema del parqueadero.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el programa
menu()
