
while True: 
    letra=input("porfavor ingrese una letra ")

    if len(letra)==1:
        letra=input("porfavor ingrese una letra ")

        vocal= "a" , "e" , "i" , "o" , "u"

        if letra == vocal:
             print("la letra ingresada es una vocal")
        else:
             print("la letra ingresada no es una vocal")
        break
    else:
        print("fuera de porfavor introducir solo una letra")
