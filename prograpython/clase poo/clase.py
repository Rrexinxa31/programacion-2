#POLIMORFISMO con método

##class Pepino():
##    def tipo(self):
##        print('vegetal')
##
##    def color(self):
##        print('verde')
##
##
##class Banano():
##    def tipo(self):
##        print('fruta')
##
##    def color(self):
##        print('amarillo')
##
##
##pep=Pepino()
##ban=Banano()

##import math
##class triangulo():
##    def __init__(self):
##        self.l1=float(input("ingrese lado 1"))
##        self.l2=float(input("ingrese lado 2"))
##        self.l3=float(input("ingrese lado 3"))
##    def peri(self):
##        print("el perimetro de esta figura es:", self.l1+self.l2+self.l3)
##    def area(self):
##        a=(self.l1+self.l2+self.l3)/2
##        area=(a*(a-self.l1)*(a-self.l2)*(a-self.l3))**0.5
##        print("el area de la figura es:", area)
##
##
##class rectangulo():
##    def __init__(self):
##        self.l1=float(input("ingrese lado 1"))
##        self.l2=float(input("ingrese lado 2"))
##    def peri(self):
##        print(f"el perimetro de esta figura es: {self.l1*2+self.l2*2}")
##    def area(self):
##        a=self.l1*self.l2
##        print("el area de la figura es:", a)
##
##class circulo():
##    def __init__(self):
##        self.r=float(input("ingrese radio"))
##    def peri(self):
##        print(f"el perimetro de esta figura es: {self.r*math.pi*2}")
##    def area(self):
##        a=self.r*math.pi
##        print("el area de la figura es:", a)
##        
##tr=triangulo()
##rt=rectangulo()


#Ejemplo herencia clase 19 octubre
class Persona():

    def __init__(self):
        self.nombre=input('ingrese su nombre ')
        self.edad=int(input('ingrese su edad '))
        self.ht=10
        
    def imprimir(self):
        print ('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años', self.ht, ' horas trabajadas')
        
class Sueldo(Persona):
    def __init__(self):
        super().__init__()#heredo atributos
        self.ht=float(input('horas trabajadas'))

    def pago(self):
        sueldot=self.ht*79000
        print(sueldot)
        

class Vida(Sueldo):
    def __init__(self):
        super().__init__()
        self.actividad=input('describa que actividad fisica realiza')

    def imprimir2(self):
        print(self.actividad)

        
class Persona1():
    def __init__(self):
        self.nombre=input('Ingrese su nombre: ')
        self.edad=int(input('Ingrese su edad: '))

    def imprimir(self):
        print ('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años')


#otra forma
# declaramos la clase persona
##class Persona2():
##    # declaramos el metodo _init_
##    def _init_(self):
##        self.nombre=input("Ingrese el nombre: ")
##        self.edad=int(input("Ingrese la edad: "))
## 
## 
##    # declaramos el metodo mostrar
##    def mostrar(self):
##        print("Nombre: ",self.nombre)
##        print("Edad: ",self.edad)
##
##
### declaramos la clase persona
##class Persona3():
##    def _init_(self,nombre, edad):
##        self.nombre=nombre
##        self.edad=edad
##
##    def imprimir(self):
##        print('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años')

        
#Herencia: recuerden que pueden heredar de cualquier clase
##class Persona1():
##    def _init_(self):
##        self.nombre=input('Ingrese su nombre: ')
##        self.edad=int(input('Ingrese su edad: '))
##
##    def imprimir(self):
##        print ('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años')
#forma 1 
##class Empleado(Persona1): #clase heredada de Persona1
##    def _init_(self):
##        super()._init_() #super es una función para llamar los atributos de la clase padre
##        self.sueldo=float(input('Ingrese su salario: '))
##
##    def imprimir(self):
##        super().imprimir()
##        print ('El salario es de: ', self.sueldo)
##
##    def impuestos(self):
##        if self.sueldo>1000000:
##            impuesto=self.sueldo*0.19
##            print(' señor ', self.nombre, ' debe pagar impuestos por un valor de $ ', impuesto)
##
##        else:
##            print (' señor ', self.nombre,'no debe pagar impuestos')
##

##class Persona3():
##    def _init_(self,nombre, edad):
##        self.nombre=nombre
##        self.edad=edad
##
##    def imprimir(self):
##        print('su nombre es ', self.nombre, ' ', 'edad ', self.edad, ' años')


#forma 2
        
##class Empleado1(Persona3):
##    def _init_(self, nombre, edad, sueldo):
##        Persona3._init_(self, nombre, edad)#informando que heredo
##        self.sueldo=sueldo #float(input('ingrese su salario '))
##
##    def impuestos (self):
##        if self.sueldo>1000000:
##            impuesto=self.sueldo*0.19
##            print('señor ', self.nombre, ' debe pagar impuesto por un valir de $ ', impuesto)
##        else:
##            print('señor ', self.nombre, 'no debe pagar impuesto')

#HERENCIA Y POLIMORFISMO

##class Empresa():
##    def seccion(self):
##        print('Bienvenido a la empresa de programación orientada a objetos')
##
##class financiera(Empresa): #depende de la clase Empresa
##    def seccion(self):
##        print('Acá se lleva la contabilidad de la empresa')
##
##class talentohumano(Empresa):  #depende de la clase Empresa
##    def seccion(self):
##        print ('Acá se hacen las entrevistas y contrata el personal')
##

##emp1=Empresa()
##emp2=financiera()
##emp3=talentohumano()
##emp1.seccion()
##emp2.seccion()
##emp3.seccion()



##cr=circulo()
