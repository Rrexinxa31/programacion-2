#12

def hallar_mayor_menor(a,b):
    numero1 = a
    numero2 = b
    return a,b
A = float(input("porfavor ingrese un numero "))
B = float(input("porfavor ingrese otro numero "))
numero1,numero2 = hallar_mayor_menor(A,B)
if A>B:
    print(numero1, " es el numeromayor y ",numero2," es el numero menor")
else:
    print(numero2, " es el numeromayor y ",numero1," es el numero menor")
