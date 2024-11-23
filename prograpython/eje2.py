import math
print("Por favor ingrese los valores para aplicar cada operacion matematica")
print("ingrese dos valores a y b para sumarlos")
print("valor de a")
a=float(input())
print("valor de b")
b=float(input())
suma=a+b
print("su suma es igual= ", suma)

print("ingrese dos valores a y b para restarlos")
print("valor de a")
a=float(input())
print("valor de b")
b=float(input())
resta=a-b
print("su resta es igual= ", resta)

print("ingrese dos valores a y b para multiplicarlos")
print("valor de a")
a=float(input())
print("valor de b")
b=float(input())
mult=a*b
print("su multiplicacion es igual= ", mult)

print("ingrese dos valores a y b para dividirlos")
print("valor de a")
a=float(input())
print("valor de b")
b=float(input())
if b == 0:
    print("division por 0")
else:
    div=a/b
    print("su division es igual= ", div)

print("engrese el valor de a para hallar su raiz")
a=float(input())
raiz=math.sqrt(a)
print("su raiz es igual=", raiz)

print("ingrese el numero y el porcentaje para hallar")
print("numero")
numero=float(input())
print("porcentaje")
porce=float(input())
result=(numero*porce)/100
print("su porcentajes es= ",result,"%")

print("ingrese el numero que quiere elevar y el numero de exponente")
print("numero a elevar")
num=float(input())
print("numero de exponente")
expo=float(input())
eleve= num**expo
print("su potencia es igual a", eleve)

        
