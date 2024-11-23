##class Cliente():
##    def __init__(self):
##        self.nombre=input('nombre')
##        self.tipocuenta=input('tipo de cuenta')
##        self.__codigo=1234 #encapsula el dato
##
##    def __cuenta(self):
##        print('cuenta de procesamiento')
##           
##    def getcodigo(self):  #con este método busca el código encapsulado
##        return self.__codigo
##
##
##cli=Cliente()
##print(cli._Cliente__codigo) #puede ver el código guardado ->1234
##cli._Cliente__cuenta()#->cuenta de procesamiento

#ejercicio 3 de encapsulamiento


import pandas as pd

class Banco():
    def __init__(self):
        print("""Bienvenido al banco
                    1.Iniciar sesion
                    2.Registrarse""")
        op=input("Ingrese la opcion")
        if op == "1":
            pass
        elif op =="2":
            self.Usuarionuevo()
        else:
            print("Opcion erronea")
    
    def Usuarionuevo(self):
        self.nombre=input('ingrese su nombre y apellidos: ')
        self.direccion=input('ingrese su dirección: ')
        self.telefono=int(input('ingrese su numero telefonico: '))
        self.tipocuenta=input('ingrese tipo de cuenta: ')
        self.apertura=float(input("ingrese dinero de apertura"))
        self.__dinero=self.apertura-50000 #float(input('ingrese dinero de apertura cuenta: '))
        self.Menu()

    def Recibo(self):
        print(self.nombre, self.direccion, self.telefono, self.tipocuenta, self.__dinero)
        return (self.nombre, self.direccion, self.telefono, self.tipocuenta, self.__dinero)

    def Retirar(self, valor):
        if valor > self.__dinero:
            print("saldo insuficiente")
        else:
            self.__dinero-=valor
        self.Menu()    
            
        

    def Consignar(self, valor):
        self.__dinero+=valor


    def Menu(self):
        print("Bienvenido al banco")
        op=input("""Ingrese la opcion
                    1.Ver recibo
                    2.Retirar
                    3.consignar""")
        if op == "1":
            self.Recibo()
        elif op=="2":
            value=float(input("Ingrese valor a retirar"))
            self.Retirar(value)
        elif op=="3":
            self.Consignar()
        else:
            print("error")
            
a=Banco()


#comentarios
###podemos acceder a un atributo privado asi:
###nombreobjeto.nombreclase__nombreatributo
##ejemplo: a.Banco__dinero     

###creación de objetos para probar el programa
##p1=Persona(1,'julian',12)
##p2=Persona(122222,'hector', 15)
##print (p1.Persona_codigo)
##print (p1.Persona_nombre)
##print (p1.edad)
##
##print (p2.Persona_codigo)
##print (p2.Persona_nombre)
##print (p2.edad)
##
##p1.nombre = 'hector julian'
##p1.saludar()
