import datetime

class UIS:
    def __init__(self):
        self.profesion=input("Ingrese profesion")
        # Solicitar al usuario que ingrese su nombre y apellido
        self.nombre_apellidos = input("Ingrese apellido y nombres: ")
        # Solicitar al usuario que ingrese su documento de identidad
        self.documento = input("Ingrese cédula: ")
        # Solicitar la fecha de nacimiento en el formato YYYY-MM-DD
        self.fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
        self.horastrabajadas = float(input("indique horas trabajadas"))
        # Calcular la edad de la persona
        self.edad = self.calcular_edad()
        # Mostrar la edad de la persona
        
       

    def imprimir(self):
         print(f"{self.nombre_apellidos} profesion {self.profesion} tiene {self.edad} años con documento {self.documento} y horas trabajadas:  {self.horastrabajadas}.")

    def calcular_edad(self):
        fecha_nacimiento_dt = datetime.datetime.strptime(self.fecha_nacimiento, "%Y-%m-%d")
        fecha_actual = datetime.datetime.now()
        edad = fecha_actual.year - fecha_nacimiento_dt.year
        if (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento_dt.month, fecha_nacimiento_dt.day):
            edad -= 1
        return edad


class vigilancia(UIS):
    def __init__(self):
        super().__init__()
        self.turno= input("Ingrese turno dia/noche")
        self.lugar= input("Ingrese el lugar del turno")

    def sueldo(self):
        self.sueldo=float(self.horastrabajadas*7000)

    def imprimir(self):
        print(f"""
                Nombre y apellido: {self.nombre_apellidos}
                Profesion: {self.profesion}
                Documento: {self.documento}
                Edad: {self.edad}
                Horas trabajadas: {self.horastrabajadas}
                Sueldo: {self.sueldo} """
              )

        








        
    
    
