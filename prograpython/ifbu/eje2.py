
import math
a=float(input("ingrese el valor a de la raiz "))
b=float(input("ingrese el valor b de la raiz "))
c=float(input("ingrese el valor c de la raiz "))
dic = b**2 - 4*a*c
if (dic>0):

        raiz1 = (-b + math.sqrt(dic))/(2*a)
        raiz1 = (-b - math.sqrt(dic))/(2*a)

        print("las raices son reales y distintas", raiz1 ,raiz2)
elif (dic==0):
        raiz = -b/(2*a)
        print("las raices reales son iguales ",raiz)
else:
        real = -b /(2*a)
        imaginaria = math.sqrt(-dic)/(2*a)
        print("las raices son complejas " ,real+imaginaria,"i" ,"Y" , real-imaginaria,"i")
