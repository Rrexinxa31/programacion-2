from datetime import datetime

#almacenar la información
JDRC_vehiculos = []
JDRC_cantidad_motos = 0
JDRC_cantidad_carros = 0
JDRC_dinero_recogido = 0

#calcular la duración en minutos entre dos tiempos dados
def JDRC_calcular_duracion(hora_entrada, hora_salida):
    formato = "%H:%M"
    entrada = datetime.strptime(hora_entrada, formato)
    salida = datetime.strptime(hora_salida, formato)
    duracion = int((salida - entrada).total_seconds() / 60)
    return duracion

#calcular el precio según el tiempo de parqueo y el tipo de vehículo
def JDRC_calcular_precio(duracion, tipo_vehiculo):
    fracciones = duracion // 15
    if tipo_vehiculo == "moto":
        return fracciones * 500
    elif tipo_vehiculo == "carro":
        return fracciones * 1000

# Menuprincipal
while True:
    print("\n--- MENÚ PARQUEADERO ---")
    print("1. Registrar entrada de vehículo")
    print("2. Registrar salida y calcular precio")
    print("3. Ver estadísticas del día")
    print("4. Salir")

    JDRC_opcion = input("Seleccione una opción: ")

    if JDRC_opcion == "1":
        JDRC_tipo_vehiculo = input("Ingrese el tipo de vehículo (moto/carro): ").lower()
        if JDRC_tipo_vehiculo not in ["moto", "carro"]:
            print("Tipo de vehículo no válido. Intente nuevamente.")
            continue
        
        JDRC_placa = input("Ingrese la placa del vehículo: ").upper()
        JDRC_hora_entrada = input("Ingrese la hora de entrada (HH:MM): ")

        # Registrar vehículo
        JDRC_vehiculos.append({
            "tipo": JDRC_tipo_vehiculo,
            "placa": JDRC_placa,
            "hora_entrada": JDRC_hora_entrada,
            "hora_salida": None,
            "duracion": None,
            "precio": None
        })

        if JDRC_tipo_vehiculo == "moto":
            JDRC_cantidad_motos += 1
        else:
            JDRC_cantidad_carros += 1

        print("Vehículo registrado con éxito.")

    elif JDRC_opcion == "2":
        JDRC_placa_salida = input("Ingrese la placa del vehículo para calcular el precio: ").upper()
        encontrado = False

        for JDRC_vehiculo in JDRC_vehiculos:
            if JDRC_vehiculo["placa"] == JDRC_placa_salida and JDRC_vehiculo["hora_salida"] is None:
                JDRC_hora_salida = input("Ingrese la hora de salida (HH:MM): ")
                JDRC_duracion = JDRC_calcular_duracion(JDRC_vehiculo["hora_entrada"], JDRC_hora_salida)
                JDRC_precio = JDRC_calcular_precio(JDRC_duracion, JDRC_vehiculo["tipo"])

                # Actualizar información del vehículo
                JDRC_vehiculo["hora_salida"] = JDRC_hora_salida
                JDRC_vehiculo["duracion"] = JDRC_duracion
                JDRC_vehiculo["precio"] = JDRC_precio

                JDRC_dinero_recogido += JDRC_precio
                encontrado = True

                print(f"Duración del parqueo: {JDRC_duracion} minutos")
                print(f"Precio a pagar: ${JDRC_precio}")
                break

        if not encontrado:
            print("No se encontró el vehículo o ya se registró la salida.")

    elif JDRC_opcion == "3":
        print("\n--- ESTADÍSTICAS DEL DÍA ---")
        print(f"Total de motos ingresadas: {JDRC_cantidad_motos}")
        print(f"Total de carros ingresados: {JDRC_cantidad_carros}")
        print(f"Dinero total recogido: ${JDRC_dinero_recogido}")

    elif JDRC_opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
