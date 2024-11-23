#nombre=input("Ingrese nombre por favor ")
#fecha=int(input("Ingrese su año de nacimiento "))
#edad= 2024-fecha

#if(edad>=18):
    #print(nombre, "tiene ", edad, "años")
#else:
    #print(nombre, "usted es menor de edad")





##lado1=float(input("Ingrese lado 1 del triangulo"))
##lado2=float(input("Ingrese lado 2 del triangulo"))
##lado3=float(input("Ingrese lado 3 del triangulo"))
##
##if(lado1+lado2>lado3 and lado1+lado3>lado2 and lado3+lado2>lado1):
##    print("Los lados pertenecen a un triangulo")
##    if(lado1==lado2==lado3):
##        print("triangulo equilatero")
##    elif(lado1!=lado2!=lado3):
##        print("triangulo escaleno")
##    else:
##        print("triangulo isosceles")
##else:
##    print("no es triangulo")


##import math
##print(""" Perimetros y areas de figuras geometricas
##    Marque: 1:cuadrado
##            2:triangulo
##            3:circurferencia
##            4:rombo
##            5:trapecio""")
##figura=input("ingrese la opcion")
##if(figura == "1"):
##    lado=float(input("ingrese el lado "))
##    peri=lado*4
##    area=lado*lado
##    print("Perimetro= ", peri, "Area= ", area)
##elif(figura=="2"):
##    lado1=float(input("Ingrese lado 1 "))
##    lado2=float(input("Ingrese lado 2 "))
##    lado3=float(input("Ingrese lado 3 "))
##    if(lado1+lado2>lado3 and lado1+lado3>lado2 and lado3+lado2>lado1):
##        peri=lado1+lado2+lado3
##        semip=peri/2
##        area=math.sqrt((semip)*(semip-lado1)*(semip-lado2)*(semip-lado3))
##        print(f"Perimetro:{round(peri,2)} Area:{round(area,2)}")
##elif(figura=="3"):
##    r=float(input("Ingrese el radio de la circurferencia "))
##    area=math.pi*r**2
##    peri=2*math.pi*r
##    print(f"Perimetro:{round(peri,2)} Area:{round(area,2)}")
##elif(figura=="4"):
    ##pass
        


##cajero=input("Ingrese una de las Opciones: Retiro, Consulta, tra, recibos")
##match cajero:
##    case "Retiro":
##        plata=int(input("Valor de retiro"))
##        print("Retiro exitoso")
##    case "Consulta":
##        print("su saldo es $150.000.000")
##    case "tra":
##        print("Transferencia exitosa")
##    case "recibos":
##        print("agua, luz, internet, gas")


##lista=["Bancolombia","Davivienda","BBVA","Bogota"]
##a=input("ingrese nombre del banco")
##b= a in lista
##if b == True:
##    print("si tenemos convenio")
##else:
##    print("no tenemos convenio")



##l=[0]
##entrada= int(input("ingrese un num positivo"))
##p=0
##while entrada>=l[p]:
##    l.append(entrada)
##    p+=1
##    entrada= int(input("ingrese un num positivo"))
##    while entrada<=l[p]:
##        print("No cumple")
##        entrada= int(input("ingrese un num positivo"))
        
    
   
##while == "4":
##    import math
##    print(""" Perimetros y areas de figuras geometricas
##        Marque: 1:cuadrado
##                2:triangulo
##                3:circurferencia
##                4:terminar
##                5:trapecio""")
##    figura=input("ingrese la opcion")
##    if(figura == "1"):
##        lado=float(input("ingrese el lado "))
##        peri=lado*4
##        area=lado*lado
##        print("Perimetro= ", peri, "Area= ", area)
##    elif(figura=="2"):
##        lado1=float(input("Ingrese lado 1 "))
##        lado2=float(input("Ingrese lado 2 "))
##        lado3=float(input("Ingrese lado 3 "))
##        if(lado1+lado2>lado3 and lado1+lado3>lado2 and lado3+lado2>lado1):
##            peri=lado1+lado2+lado3
##            semip=peri/2
##            area=math.sqrt((semip)*(semip-lado1)*(semip-lado2)*(semip-lado3))
##            print(f"Perimetro:{round(peri,2)} Area:{round(area,2)}")
##    elif(figura=="3"):
##        r=float(input("Ingrese el radio de la circurferencia "))
##        area=math.pi*r**2
##        peri=2*math.pi*r
##        print(f"Perimetro:{round(peri,2)} Area:{round(area,2)}")
##
##        while figura =="4":
##            print("fin")
            
    
#for chao in range(1,10,1):
   # print(chao)

##lista=[13,25,55,12,33]
##for hoy in lista:
##    print(hoy)


i=int(input("ingrese un num"))
for hoy in range(1,21):
    a=hoy*i
    print(hoy,"X",i,"=",a)
    
      
