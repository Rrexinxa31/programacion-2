##a="si"
##b=a.lower()
##while b=="si":
##    cont=0
##    cadena=input("Ingrese una cadena de texto\n")
##    for letra in cadena:
##        if(letra.isupper() == True):
##            cont+=1
##    print(cont)
##    a=input("Desea escribir otra frase")


###Revise el siguiente código: lealo y comentelo indicando que función cumple cada sección.
##import math as m
##import random
##import sys
##
###calculadora
##u=True
##while (u==True):
##    print('''###################################
##            CALCULADORA
##            1. suma
##            2. resta
##            3. producto
##            4. cociente
##            5. porcentajes
##            6. comparación pares e impares
##            7. trigonometría
##            ##################################''')
##    a=int(input('ingrese la accion'))
##    print('digite los números de la operación')
##    x=float(input('n1\n'))
##    y=float(input('n2\n'))
##    if a==1:
##        print('la suma: ', x+y)
##    elif a==2:
##        print('la resta es: ', x-y)
##    elif a==3:
##        print('el prodcuto es: ', x*y)
##    elif a==4:
##        print('el cociente es: ', x/y)
##    elif a==5:
##        print( 'el ', x, ' porciento de ', y, ' es ', (x*y)/100)
##    elif a==6:
##        if x%2==0 and y%2==0:
##            print('el numero ', x, 'y el numero ', y, ' son pares')
##        elif x%2==0 and y%2!=0:
##            print('el numero ', x, ' es par y el numero ', y, ' es impar')
##        elif x%2!=0 and y%2==0:
##            print('el numero ', x, ' es impar y el numero ', y, ' es par')
##        else:
##            print('el numero ', x, 'y el numero ', y, 'son impares')
##    elif a==7:
##        x=float(input("Ingrese los grados para convertirlos a radianes"))
##        r=m.radians(x)
##        print("Sus grados en radianes=", r)
##        sen=m.sin(r)
##        cos=m.cos(r)
##        print("Coseno= ", cos , "Seno= ", sen)
##       
##    print ('Desea continuar con la ejecución del programa: Marque Si o No')
##    u=input()
##    if u=='Si' or u=='si' or u=='SI':
##        u=True
##
##    else:
##        u=False


##def hoy():
##    print("Bienvenido")
##
##def Sumar(num1, num2):
##    global resul
##    resul=num1+num2
##    return resul #return debe tener donde almacenarse
##a=float(input("ingrese un numero"))
##b=float(input("ingrese un numero"))
##c=Sumar(a,b)
##print(c)

##def perimetro_triangulo ( cateto1 : float ,cateto2:float)->float:  #Aqui se define los parametros como flotantes y que nos de flotantes
##    hipotenusa=calcular_hip(cateto1,cateto2)#aqui se returna el dato de la hip de la otra funcion
##    return cateto1+cateto2+hipotenusa #aqui los valores se retornan a la variable perimetro se hace la suma de los datos ingresados y los hallados con la otra funcion
##
##def calcular_hip(cateto1:float,cateto2:float)->float: #aqui igual los parametros se definen como flotantes para que nos de flotantes
##    suma_cuadrados=(cateto1**2)+(cateto2**2)#aqui hacemos pitagoras
##    hipotenusa=pow(suma_cuadrados,0.5)#aqui se termina dde hallar la hip con la suma de cats al cuadrado en raiz
##    return hipotenusa#aqui me lo retorna al primer bloque o funcion para hallar el perimetro

##cadena_cat_1=input("Indique la longitud del primer cateto: ")#aqui me pide un dato en cadena
##cadena_cat_2=input("Indique la longitud del segundo cateto: ")#aqui igual
##cat_1=float(cadena_cat_1)#aqui me encierra el dato anterior y hace que sean flotantes
##cat_2=float(cadena_cat_2)#aqui igual como por ejemplo hacer a=float(input()) solo la estoyt meteiendo dentro de otra
##perimetro=perimetro_triangulo(cat_1,cat_2)#aqui es donde retorna la el valor de la primera funcion
##print("El perímetro de un triángulo rectángulo que tenga catetos de longitud",cat_1,"y",cat_2,"es",perimetro)

#preg1 rta: Calcular el perimetro mediante sus catetos.
#preg 2 rta: pide dos datos, dos catetos.
#preg3 rta: primero se ejecuta las entradas para los catetos, luego la segunda funcion para hallar la hipotenusa y
#tercero la primera funcion para despues mandar el dato al imprimir los catetos y el perimetro



##def area_perimetro_rectangulo(base,altura):
##    perimetro=2*(base+altura)
##    area=base*altura
##    return perimetro,area
##bas=float(input("Ingrese la base del rectangulo"))
##alt=float(input("Ingrese la altura del rectangulo"))
##perimetro, area= area_perimetro_rectangulo(bas,alt)
##print("Perimetro= ", perimetro, "Area= ", area)


def Suma():
    a= float(input("num"))
    b= float(input("num1"))
    print(a+b)
    menu()
def Resta():
    a= float(input("num"))
    b= float(input("num1"))
    print(a-b)
    menu()    
def Producto():
    a= float(input("num"))
    b= float(input("num1"))
    print(a*b)
    menu()
def Cociente():
    a= float(input("num"))
    b= float(input("num1"))
    print(a/b)
    menu()
def menu():
    print("""Seleccione
                        1:suma
                        2:resta
                        3:prodecto
                        4:cociente
                        5:salir    """)
    op=int(input("Opcion deseada"))
    while op>=1 and op<=5:
        if op == 1:
            Suma()
        elif op==2:
            Resta()
        elif op==3:
            Producto()
        elif op==4:
            Cociente()
        elif op==5:
            exit()
        else:
            print("Error")
menu()            
        
        
    
    
