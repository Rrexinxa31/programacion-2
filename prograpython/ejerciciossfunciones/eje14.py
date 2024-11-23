#14

def relacion(a,b):
    numero1 = a
    numero2 = b
    return a,b
A = float(input("porfavor ingrese un numero "))
B = float(input("porfavor ingrese otro numero "))
numero1,numero2 = relacion(A,B)
if A==B:
    print("empate")
elif A>B:
    print("true")
elif A<B:
    print("false")
