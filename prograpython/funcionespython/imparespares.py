import random
lista=[]
n=int(input("Ingrese tamaño de lista"))
for i in range(n):
    lista.append(random.randint(1,100))


def separar(lista):
    lista.sort()
    pares=[]
    impares=[]
    for numero in lista:
        if numero % 2 ==0:
            pares.append(numero)
        else:
            impares.append    
        return pares , impares    
pares,impares=separar(lista)
print("Impares", impares)
print("Pares", pares)