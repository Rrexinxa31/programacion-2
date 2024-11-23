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
    with open('zoologico.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Especie", "Edad", "Tamaño", "Peso", "Altura", "Fecha de Ingreso", "Género", "Tipo de Alimento", "Horarios de Comida", "Vacunas", "Enfermedades"])
        for animal in animals:
            writer.writerow(animal.obtener_datos())

# Funcion para leer y mostrar los datos de los animales desde el archivo CSV
def mostrar_animales():
    try:
        with open('zoologico.csv', mode='r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Leer las cabeceras
            print(f"{headers[0]:<15} {headers[1]:<5} {headers[2]:<10} {headers[3]:<5} {headers[4]:<7} {headers[5]:<15} {headers[6]:<10} {headers[7]:<15} {headers[8]:<25} {headers[9]:<20} {headers[10]:<15}")
            for row in reader:
                print(f"{row[0]:<15} {row[1]:<5} {row[2]:<10} {row[3]:<5} {row[4]:<7} {row[5]:<15} {row[6]:<10} {row[7]:<15} {row[8]:<25} {row[9]:<20} {row[10]:<15}")
    except FileNotFoundError:
        print("El archivo zoologico.csv no se encuentra. Asegúrate de guardar datos antes de intentar mostrar.")

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
    JDRC_horarios_comida = input("Horarios de comida (separados por coma): ")
    JDRC_vacunas = input("Vacunas del animal (separadas por coma): ")
    JDRC_enfermedades = input("Enfermedades del animal: ")

    # Crear una instancia del nuevo animal
    nuevo_animal = Animal(JDRC_especie, JDRC_edad, JDRC_tamano, JDRC_peso, JDRC_altura, JDRC_fecha_ingreso, JDRC_genero, JDRC_tipo_alimento, JDRC_horarios_comida, JDRC_vacunas, JDRC_enfermedades)
    return nuevo_animal

# Instanciacin de los animales ya existentes
animal1 = Animal("León", 5, "Grande", 190, 1.2, datetime(2018, 5, 10).strftime("%Y-%m-%d"), "Macho", "Carnívoro", "9:00 AM, 5:00 PM", "Vacuna A, Vacuna B", "Ninguna")
animal2 = Animal("Elefante", 8, "Gigante", 6000, 3.0, datetime(2016, 7, 15).strftime("%Y-%m-%d"), "Hembra", "Herbívoro", "8:00 AM, 4:00 PM", "Vacuna C", "Lesión en la pata")
animal3 = Animal("Jirafa", 4, "Alta", 800, 4.5, datetime(2020, 2, 20).strftime("%Y-%m-%d"), "Macho", "Herbívoro", "7:30 AM, 3:30 PM", "Vacuna D", "Ninguna")
animal4 = Animal("Tigre", 6, "Grande", 220, 1.1, datetime(2017, 11, 5).strftime("%Y-%m-%d"), "Hembra", "Carnívoro", "10:00 AM, 6:00 PM", "Vacuna E", "Enfermedad respiratoria")
animal5 = Animal("Cebra", 3, "Mediana", 300, 1.4, datetime(2021, 3, 12).strftime("%Y-%m-%d"), "Macho", "Herbívoro", "8:00 AM, 5:00 PM", "Vacuna F", "Ninguna")
animal6 = Animal("Koala", 2, "Pequeño", 15, 0.6, datetime(2022, 9, 30).strftime("%Y-%m-%d"), "Hembra", "Herbívoro", "9:30 AM, 4:30 PM", "Vacuna G", "Infección ocular")

# Lista de animales existentes
animales = [animal1, animal2, animal3, animal4, animal5, animal6]

# Ingresar nuevos animales
while len(animales) < 15:
    respuesta = input("¿Deseas ingresar un nuevo animal? (s/n): ")
    if respuesta.lower() == "s":
        nuevo_animal = ingresar_animal()
        animales.append(nuevo_animal)
    else:
        break

# Guardar todos los animales en el archivo CSV
guardar_datos_animales(animales)

# Mostrar los datos de los animales
print("\nDatos de los animales en el zoológico:")
mostrar_animales()
