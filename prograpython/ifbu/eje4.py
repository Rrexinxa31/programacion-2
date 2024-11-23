
cantidad=float(input("ingrese la cantidad que desea convertir "))
print(""" Seleccione la opcion en la que va a ingrear la cantidad:
1:Metro
2:Kilometro
3:Centimetros
4:Millas
5:Yardas
6:Pulgadas
7:salir""")
op=int(input("opcion deseada "))
while op>=1 and op<=7:
    print(""" Seleccione la opcion a la que va a convertir la cantidad:1:Metro
            2:Kilometro
            3:Centimetros
            4:Millas
            5:Yardas
            6:Pulgadaas
            7:salir""")
    op2=int(input("opcion deseada "))
    while op2>=1 and op<=7:
        if op==1 and op2==1:
            print("la opcion a convertir es la misma intentelo otra vez")
        elif op==2 and op2==2:
            print("la opcion a convertir es la misma intentelo otra vez")
        elif op==3 and op2==3:
            print("la opcion a convertir es la misma intentelo otra vez")
        elif op==4 and op2==4:
            print("la opcion a convertir es la misma intentelo otra vez")
        elif op==5 and op2==5:
            print("la opcion a convertir es la misma intentelo otra vez")
        elif op==6 and op2==6:
            print("la opcion a convertir es la misma intentelo otra vez")
        elif op==1 and op==2:
            res = cantidad/1000
            print("la cantidad de kilometros son ",res)
        elif op==2 and op2==1:
            res = cantidad*1000
            print("la cantidad de metros son ",res)
        elif op==1 and op2==3:
            res = cantidad*100
            print("la cantidad de centimetros son ",res)
        elif op==3 and op2==1:
            res = cantidad/100
            print("la cantidad de metros son ",res)
        elif op==1 and op2==4:
            res = cantidad/1.609
            print("la cantidad de millas son ",res)
        elif op==4 and op2==1:
            res = cantidad/1.609
            print("la cantidad de metros son ",res)
        elif op==1 and op2==5:
            res = cantidad*1.094
            print("la cantidad de yardas son ",res)
        elif op==5 and op2==1:
            res = cantidad/1.094
            print("la cantidad de metros son ",res)
        elif op==1 and op2==6:
            res = cantidad*39.37
            print("la cantidad de pulgadas son ",res)
        elif op==6 and op2==1:
            res = cantidad/39.37
            print("la cantidad de metros son ",res)
        elif op==2 and op2==3:
            res = cantidad*100000
            print("la cantidad de centimetros son son ",res)
        elif op==3 and op2==2:
            res = cantidad/100000
            print("la cantidad de kilometros son ",res)
        elif op==2 and op2==4:
            res = cantidad/1.609
            print("la cantidad de millas son ",res)
        elif op==4 and op2==2:
            res = cantidad*1.609
            print("la cantidad de kilometros son ",res)
        elif op==2 and op2==5:
            res = cantidad*1094
            print("la cantidad de yardas son ",res)
        elif op==5 and op2==2:
            res = cantidad/1094
            print("la cantidad de kilometros son ",res)
        elif op==2 and op2==6:
            res = cantidad*39370
            print("la cantidad de pulgadas son ",res)
        elif op==6 and op2==2:
            res = cantidad/39370
            print("la cantidad de kilometros son ",res)
        elif op==3 and op2==4:
            res = cantidad/160900
            print("la cantidad de millas son ",res)
        elif op==4 and op2==3:
            res = cantidad*160900
            print("la cantidad de centimetros son ",res)
        elif op==3 and op2==5:
            res = cantidad/91.44
            print("la cantidad de yardas son ",res)
        elif op==5 and op2==3:
            res = cantidad*91.44
            print("la cantidad de centimetros son ",res)
        elif op==3 and op2==6:
            res = cantidad/2.54
            print("la cantidad de pulgadas son ",res)
        elif op==6 and op2==3:
            res = cantidad*2.54
            print("la cantidad de centimetros son ",res)
        elif op==4 and op2==5:
            res = cantidad*1760
            print("la cantidad de yardas son ",res)
        elif op==5 and op2==4:
            res = cantidad/1760
            print("la cantidad de millas son ",res)
        elif op==4 and op2==6:
            res = cantidad*63360
            print("la cantidad de pulgadas son ",res)
        elif op==6 and op2==4:
            res = cantidad/63360
            print("la cantidad de millas son ",res)
        elif op==5 and op2==6:
            res = cantidad*36
            print("la cantidad de pulgadas son ",res)
        elif op==6 and op2==5:
            res = cantidad/36
            print("la cantidad de yardas son ",res)
        else:
         print("Error en la opción. Inténtalo de nuevo.")

         print("\nSeleccione una nueva opción o ingrese 7 para salir:")
         op = int(input("Opción deseada: "))


        if op == 7:
          print("Gracias por usar el convertidor. ¡Adiós!")
          break
    
