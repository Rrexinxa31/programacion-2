#13
  
def inversa(cadena):
    cadenainvertida = ""
    for caracter in cadena:
        cadenainvertida = caracter+cadenainvertida
    return cadenainvertida
palabra = input("porfavor ingrese la palabra a invertir ")
res = inversa(palabra)
print(res)
