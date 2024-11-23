
nombre=input("porfavor ingrese su nombre")
apellido=input("porfavor ingrese su apellido")
documento=input("porfavor ingrese su documento de identidad")
sueldo=float(input("porfavor ingrese su salario"))

mini=1300000
print(nombre)
print(apellido)
print(documento)
print("el minimo es de $",mini, "pesos colombianos ")
if(sueldo>mini):
    print(nombre, "gana mas de el minimo ")
elif(sueldo==mini):
    print(nombre, "gana lo mismo que el minimo ")

