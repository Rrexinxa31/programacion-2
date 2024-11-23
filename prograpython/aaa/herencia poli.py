from datetime import datetime as dt

class UIS():
    def __init__(self):
        self.jdrc_nombre_y_apellidos = input("Ingresar nombre y apellidos: ")
        self.jdrc_documento_de_identidad = int(input("Ingresar su documento de identidad: "))
        self.jdrc_fecha_de_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

        try:
            self.jdrc_fecha_de_nacimiento = dt.strptime(self.jdrc_fecha_de_nacimiento, "%d/%m/%Y")
            # Formateamos la fecha de nacimiento a un string con el formato deseado
            self.jdrc_fecha_formateada = self.jdrc_fecha_de_nacimiento.strftime("%d/%m/%Y")
            fecha_actual = dt.now()
            self.jdrc_edad = fecha_actual.year - self.jdrc_fecha_de_nacimiento.year
            if (fecha_actual.month, fecha_actual.day) < (self.jdrc_fecha_de_nacimiento.month, self.jdrc_fecha_de_nacimiento.day):
                self.jdrc_edad -= 1

        except ValueError:
            print("La fecha ingresada no es válida. Asegúrate de usar el formato correcto (dd/mm/aaaa).")
            UIS()

        self.jdrc_profesion = input("Ingresar su profesion: ")
        self.jdrc_horas_de_trabajo = int(input("Ingresar la horas de trabajo: "))

    def Mostrar(self):
        print("Sus nombre y apellidos son: ", self.jdrc_nombre_y_apellidos, ", su documento es:", self.jdrc_documento_de_identidad, ", fecha de nacimiento:", self.jdrc_fecha_formateada,
              ", edad: ", self.jdrc_edad, ", profesion: ", self.jdrc_profesion, "y horas de trabajo diarias: ", self.jdrc_horas_de_trabajo)


class Vigilancia(UIS):

    def __init__(self):
        print("VIGILANCIA")
        super().__init__()
        self.jdrc_turno = input("Ingrese su Turno si es diurno o nocturno: ")
        self.jdrc_lugar = input("Lugar en donde se ubica su trabajo: ")
        self.jdrc_sueldot = 0

    def sueldo(self):
        self.jdrc_sueldot = self.jdrc_horas_de_trabajo * 100000

    def Mostrar(self):
        self.sueldo()
        print("Sus nombre y apellidos son: ", self.jdrc_nombre_y_apellidos, ", su documento es:", self.jdrc_documento_de_identidad, ", fecha de nacimiento:", self.jdrc_fecha_formateada, 
              ", edad: ", self.jdrc_edad, ", profesion: ", self.jdrc_profesion, ", horas de trabajo diarias: ", self.jdrc_horas_de_trabajo, ", Trabaja en el turno: ", 
              self.jdrc_turno, ", en el lugar llamado: ", self.jdrc_lugar, "y su sueldo es de: ", self.jdrc_sueldot)
    
    def funciones(self):
        print("""FUNCIONES
                  1. Cuidar los elementos y personas en el recinto
                  2. Vigilancia por posibles hechos no legales en el recinto
                  3. """)


class Administrativos(UIS):

    def __init__(self):
        print("ADMINISTRATIVOS")
        super().__init__()
        self.jdrc_dependencia = input("Que dependencia está?: ")

    def sueldo(self):
        self.jdrc_sueldot = self.jdrc_horas_de_trabajo * 200000

    def Mostrar(self):
        self.sueldo()
        print("Sus nombre y apellidos son: ", self.jdrc_nombre_y_apellidos, ", su documento es:", self.jdrc_documento_de_identidad, ", fecha de nacimiento:", self.jdrc_fecha_formateada,
              ", edad: ", self.jdrc_edad, ", profesion: ", self.jdrc_profesion, ", horas de trabajo diarias: ", self.jdrc_horas_de_trabajo, ", su dependencia es: ", 
              self.jdrc_dependencia, "y su sueldo es de: ", self.jdrc_sueldot)

    def funciones(self):
        print("""FUNCIONES
                  1. Hacer los trámites tanto contables como académicos de los estudiantes en su ingreso
                  2. Prestar ayuda en problemas contables o académicos
                  3. """)


class Auxiliares(Vigilancia):

    def __init__(self):
        print("AUXILIARES")
        super().__init__()

    def funciones(self):
        print("""FUNCIONES
                  1. Brindar ayuda a los estudiantes en varios temas sin incurrir en los administrativos
                  2. 
                  3. """)
