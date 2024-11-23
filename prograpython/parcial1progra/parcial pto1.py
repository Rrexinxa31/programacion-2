import csv

# este es el usuario del profe
JDRC_usuario = "profe123"
JDRC_contraseña = "3130"
intentos_maximos = 3
n = 0  # numero de intentos

def JDRC_inicio():
    global n
    while n < intentos_maximos:
        # pide usuarioo y contraseña
        JDRC_inicio_usuario = input("Ingrese usuario: ")
        JDRC_inicio_contraseña = input("Ingrese contraseña: ")

        # verifica el inicio desesionn
        if JDRC_inicio_usuario == JDRC_usuario and JDRC_inicio_contraseña == JDRC_contraseña:
            print("Inicio de sesión correcto.")
            mostrar_asignaturas()  # muestra las asignaturas
            break
        else:
            print("Contraseña o usuario incorrectos.")
            n += 1  # suma uno en uno los intentos
            
            # si se pasan los intentos muere el prgrama
            if n == intentos_maximos:
                print("Máximo de intentos alcanzado. Intente más tarde.")

def mostrar_asignaturas():
    global JDRC_asignatura
    while True:
        # muestrasignaturas
        JDRC_asignatura = input("""ASIGNATURAS
                                    1. ECUACIONES
                                    2. PROGRAMACION2
                                    3. DIBUJO
                                    Ingrese el número de la asignatura: """)
        
        if JDRC_asignatura in ['1', '2', '3']:
            JDRC_menu_asignaturas(JDRC_asignatura)
            break  # esto nos saca del bucle si el inicio es correcto
        else:
            print("Opción no válida. Intente nuevamente.")

def JDRC_menu_asignaturas(asignatura):
    while True:
        JDRC_registromenu = input("""Seleccione una opción:
                                     1. Registrar asistencia
                                     2. Ver informe de asistencia
                                     3. Salir
                                     Ingrese el número de la opción: """)

        if JDRC_registromenu == '1':
            registrar_asistencia(asignatura)
        elif JDRC_registromenu == '2':
            ver_informe_asistencia(asignatura)
        elif JDRC_registromenu == '3':
            print("Saliendo del menú de asignaturas.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def registrar_asistencia(asignatura):
    # hace el registro de la asignatura
    nombre_estudiante = input("Ingrese el nombre del estudiante: ")
    fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
    hora = input("Ingrese la hora (HH:MM): ")

    # guarda en el archivo csv la asistencia
    with open('asistencia.csv', mode='a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow([asignatura, nombre_estudiante, fecha, hora])
    
    print(f"Asistencia registrada para {nombre_estudiante} en la asignatura {asignatura}.")

def ver_informe_asistencia(asignatura):
    # nos muestra lo registrado en el archivo csv
    try:
        with open('asistencia.csv', mode='r') as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            print(f"Informe de asistencia para la asignatura {asignatura}:")
            for fila in lector_csv:
                if fila[0] == asignatura:  # compruba si la asignatura es la correcta
                    print(f"- Estudiante: {fila[1]}, Fecha: {fila[2]}, Hora: {fila[3]}")
    except FileNotFoundError:
        print("No hay registros de asistencia. El archivo no fue encontrado.")

# incia de nuevo
JDRC_inicio()
