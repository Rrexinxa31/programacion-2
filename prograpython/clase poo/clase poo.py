class Alumno:
    def __init__(self):
        self.nombre=input("Ingrese nombre")
        self.apellido=input("Ingrese apellido")
        self.nota=int(input("Ingrese nota"))
        self.codigo=int(input("Ingrese codigo de estudiante"))
    def imprimir(self):
         print("Nombre: ",self.nombre)
         print("Apellido",self.apellido)
         print("Nota: ",self.nota)
         print("Codigo estudiante",self.codigo)

    def resultado(self):
        if self.nota < 5:
            print("El alumno ha suspendido") 
        else: 
            print("El alumno ha aprobado")

alumno1=Alumno()
alumno1.imprimir()
alumno1.resultado()
while True:
    alumnos= Alumno()
            
 
##alumno1=Alumno() 
##alumno2=Alumno() 
##alumno1.inicializar("ivan",8) 
##alumno2.inicializar("juan",4) 
##alumno1.imprimir() 
##alumno1.resultado() 
##alumno2.imprimir() 
##alumno2.resultado()

##class Persona:
##    def __init__(self):
##        self.nombre=input("Ingrese nombre")
##        self.edad=int(input("Ingreae edad"))
##    def imprimir(self):
##        print("Nombre: ",self.nombre)
##        print("Edad: ",self.edad)
##    def mayor_edad(self):
##        if self.edad >= 18:
##            print("Es mayor de edad")
##        else:
##            print("No es mayor de edad")
##persona1=Persona()
##persona1.inicializar("Ivan",23)
##persona2=Persona()
##persona2.inicializar("Carlos",17)
##persona1.imprimir()
##persona1.mayor_edad()
##persona2.imprimir()
##persona2.mayor_edad()


##class Calculadora:
##    def __init__(self):
##        self.valor1=int(input("Ingrese el primer valor: "))
##        self.valor2=int(input("Ingrese el segundo valor: "))
##        self.menu()
##    def suma(self):
##        suma=self.valor1+self.valor2
##        print("El resultado de la suma de los valores es: ",suma)
##    def resta(self):
##        resta=self.valor1-self.valor2
##        print("El resultado de la resta de los valores es: ",resta)
##    def multiplicacion(self):
##        pro=self.valor1*self.valor2
##        print("El resultado de la multiplicación de los valores es: ",pro)
##    def division(self):
##        div=self.valor1/self.valor2
##        print("El resultado de la división de los valores es: ",div)
##    def imprimir(self):
##        print("Los valores son: ")
##        print("Valor 1: ",self.valor1)
##        print("Valor 2: ",self.valor2)
##    def menu(self):
##        op=input("ingrese 1. suma 2. resta 3. multiplicacion 4. division 5. imprimir ")
##        if op == "1":
##            self.suma()
##        elif op == "2":
##            self.resta()
##        elif op == "3":
##            self.multiplicacion()
##        elif op == "4":
##            self.division()
##        elif op == "5":
##            self.imprimir()
##        elif op == "6":
##            exit
##        else:
##            print("error")
##            self.menu
##            
##while True:
##    calcular=Calculadora()
##calcular.imprimir()
##calcular.suma()
##calcular.resta()
##calcular.multiplicacion()
##calcular.division()


##class Persona():
##    nombre='daniel'
##    apellido='cerinza'
##    trabajo='estudiante'
##
##    def mostrar(self):
##        print(f"su nombre es {self.nombre}, con apellido {self.apellido} y su trabajo es {self.trabajo}")
##    def si(self):
##        print("somos lo mejor de la uis")







