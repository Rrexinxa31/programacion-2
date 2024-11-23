import csv
from datetime import datetime

# Clase Usuario para manejar el inicio de sesión
class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def iniciar_sesion(self):
        usuario = input("Ingresa tu usuario: ")
        if usuario == self.nombre:
            contraseña = input("Ingresa tu contraseña: ")
            if contraseña == self.contraseña:
                print(f"Bienvenido {self.nombre}!")
                return True
            else:
                print("Contraseña incorrecta.")
                return False
        else:
            print("Usuario no encontrado.")
            return False

# Clase Asignatura para manejar los estudiantes por materia
class Asignatura:
    def __init__(self, nombre, estudiantes):
        self.nombre = nombre
        self.estudiantes = estudiantes

# Clase Asistencia para registrar y guardar la asistencia
class Asistencia:
    def __init__(self, asignaturas):
        self.asignaturas = asignaturas

    def registrar_asistencia(self):
        fecha_actual = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Obtener la fecha y hora actual
        for asignatura in self.asignaturas:
            print(f"\nRegistrando asistencia para {asignatura.nombre}:")
            asistencia = []
            for estudiante in asignatura.estudiantes:
                presente = input(f"¿{estudiante} está presente? (1 para sí, 0 para no): ")
                asistencia.append([asignatura.nombre, estudiante, presente, fecha_actual])

            # Guardar la asistencia en el archivo CSV
            self.guardar_asistencia(asistencia)

    def guardar_asistencia(self, asistencia):
        try:
            with open('asistencia11.csv', mode='a', newline='') as archivo_csv:
                escritor_csv = csv.writer(archivo_csv)
                for registro in asistencia:
                    escritor_csv.writerow(registro)
            print("Asistencia guardada exitosamente.")
        except Exception as e:
            print(f"Error al guardar la asistencia: {e}")

    def mostrar_reporte_asistencia(self):
        try:
            with open('asistencia11.csv', mode='r') as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                print("\n--- Reporte de Asistencia ---")
                for fila in lector_csv:
                    print(f"Asignatura: {fila[0]}, Estudiante: {fila[1]}, Asistencia: {'Presente' if fila[2] == '1' else 'Ausente'}, Fecha: {fila[3]}")
        except FileNotFoundError:
            print("El archivo de asistencia no existe aún.")
        except Exception as e:
            print(f"Error al leer el archivo de asistencia: {e}")

# Función principal
def main():
    # Crear usuarios
    usuarios = [Usuario("admin1", "1234"), Usuario("admin2", "5678"), Usuario("admin3", "9012")]

    # Crear las asignaturas y estudiantes
    ecuaciones = Asignatura("Ecuaciones", ["Juan", "Daniel"])
    programacion = Asignatura("Programación 2", ["Rueda", "Cerinza", "Felipe"])
    dibujo = Asignatura("Dibujo", ["Angela"])
    
    # Crear instancia de Asistencia con las asignaturas
    asistencia = Asistencia([ecuaciones, programacion, dibujo])

    # Iniciar sesión
    usuario_valido = False
    for usuario in usuarios:
        if usuario.iniciar_sesion():
            usuario_valido = True
            break

    # Registrar asistencia si el usuario inició sesión correctamente
    if usuario_valido:
        asistencia.registrar_asistencia()
        # Mostrar reporte después de registrar la asistencia
        asistencia.mostrar_reporte_asistencia()
    else:
        print("No se pudo iniciar sesión.")

if __name__ == "__main__":
    main()
