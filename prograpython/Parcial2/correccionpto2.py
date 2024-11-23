import csv
from datetime import datetime

# Clase Animal
class Animal:
    def __init__(self, JDRC_especie, JDRC_edad, JDRC_tamano, JDRC_peso, JDRC_altura, JDRC_fecha_ingreso, JDRC_genero, JDRC_tipo_alimento, JDRC_horarios_comida, JDRC_vacunas, JDRC_enfermedades):
        self.JDRC_especie = JDRC_especie
        self.JDRC_edad = JDRC_edad
        self.JDRC_tamano = JDRC_tamano
        self.JDRC_peso = JDRC_peso
        self.JDRC_altura = JDRC_altura
        self.JDRC_fecha_ingreso = JDRC_fecha_ingreso
        self.JDRC_genero = JDRC_genero
        self.JDRC_tipo_alimento = JDRC_tipo_alimento
        self.JDRC_horarios_comida = JDRC_horarios_comida
        self.JDRC_vacunas = JDRC_vacunas
        self.JDRC_enfermedades = JDRC_enfermedades
    
    def obtener_datos(self):
        return [self.JDRC_especie, self.JDRC_edad, self.JDRC_tamano, self.JDRC_peso, self.JDRC_altura, self.JDRC_fecha_ingreso, self.JDRC_genero, self.JDRC_tipo_alimento, self.JDRC_horarios_comida, self.JDRC_vacunas, self.JDRC_enfermedades]

# Función para guardar los datos en un archivo CSV
def guardar_datos_animales(animals):
    with open('zoologico1.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Especie", "Edad", "Tamaño", "Peso", "Altura", "Fecha de Ingreso", "Género", "Tipo de Alimento", "Horarios de Comida", "Vacunas", "Enfermedades"])
        for animal in animals:
            writer.writerow(animal.obtener_datos())

# Funcion para leer y mostrar los datos de los animales desde el archivo CSV
def mostrar_animales():
    try:
        with open('zoologico1.csv', mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Leer las cabeceras
            print(f"{headers[0]:<15} {headers[1]:<5} {headers[2]:<10} {headers[3]:<5} {headers[4]:<7} {headers[5]:<15} {headers[6]:<10} {headers[7]:<15} {headers[8]:<25} {headers[9]:<20} {headers[10]:<15}")
            for row in reader:
                print(f"{row[0]:<15} {row[1]:<5} {row[2]:<10} {row[3]:<5} {row[4]:<7} {row[5]:<15} {row[6]:<10} {row[7]:<15} {row[8]:<25} {row[9]:<20} {row[10]:<15}")
    except FileNotFoundError:
        print("El archivo zoologico.csv no se encuentra. Asegúrate de guardar datos antes de intentar mostrar.")

# Validar horarios de comida
def validar_horarios():
    while True:
        horarios = input("Horarios de comida (formato HH:MM AM/PM, separados por comas): ")
        try:
            # Dividimos los horarios por comas y validamos cada uno
            horarios_list = [datetime.strptime(h.strip(), "%I:%M %p").strftime("%I:%M %p") for h in horarios.split(",")]
            return ", ".join(horarios_list)  # Retornamos los horarios validados y formateados
        except ValueError as e:
            print("Formato inválido. Asegúrate de usar el formato HH:MM AM/PM y separarlos por comas.")
            print("Ejemplo válido: 09:00 AM, 05:00 PM")

# Funcion para ingresar un nuevo animal
def ingresar_animal():
    JDRC_especie = input("Especie del animal: ")
    JDRC_edad = int(input("Edad del animal: "))
    JDRC_tamano = input("Tamaño del animal (Pequeño, Mediano, Grande, Gigante): ")
    JDRC_peso = float(input("Peso del animal (en kg): "))
    JDRC_altura = float(input("Altura del animal (en metros): "))
    JDRC_fecha_ingreso = datetime.strptime(input("Fecha de ingreso (YYYY-MM-DD): "), "%Y-%m-%d").date()
    JDRC_genero = input("Género del animal (Macho/Hembra): ")
    JDRC_tipo_alimento = input("Tipo de alimento (Carnívoro, Herbívoro, Omnívoro): ")
    JDRC_horarios_comida = validar_horarios()
    JDRC_vacunas = input("Vacunas del animal (separadas por coma): ")
    JDRC_enfermedades = input("Enfermedades del animal: ")

    # Crear una instancia del nuevo animal
    nuevo_animal = Animal(JDRC_especie, JDRC_edad, JDRC_tamano, JDRC_peso, JDRC_altura, JDRC_fecha_ingreso, JDRC_genero, JDRC_tipo_alimento, JDRC_horarios_comida, JDRC_vacunas, JDRC_enfermedades)
    return nuevo_animal

# Lista de animales existentes
animales = []

# Menú principal
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Ingresar nuevo animal")
        print("2. Mostrar animales")
        print("3. Guardar datos")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nuevo_animal = ingresar_animal()
            animales.append(nuevo_animal)
        elif opcion == "2":
            mostrar_animales()
        elif opcion == "3":
            guardar_datos_animales(animales)
            print("Datos guardados correctamente.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

# Ejecutar menú
menu()
