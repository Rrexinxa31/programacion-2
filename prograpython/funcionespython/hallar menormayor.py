a=int(input("ingrese un numero a"))
b=int(input("ingrese un numero b"))

def hallar_mayor_menor(a,b):

    if a>b:
        mayor=print("El mayor es ", a)
        menor=print("El menor es ", b)
    else:
        mayor=print("El mayor es ", b)
        menor=print("El menor es ", a)   
    return   mayor,menor
mayor,menor=hallar_mayor_menor(a,b)
print("El mayor= ", mayor, "El menor= ", menor) 
