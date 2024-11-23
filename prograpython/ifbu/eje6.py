estudiantes=[]

numero=int(input("Ingrese la cantidad de estudiantes: "))

for i in range(numero):
    nombre=input("ingrese el nombre del estudiante del estudiante ")
    estudiantes.append(nombre)
buscar = input("ingrese el nombre que desea buscar ")
if buscar in estudiantes:
    print(buscar, "está en la lista de estudiantes")
else:
    print(buscar, "no está en la lista de estudiantes")
 Inicializar variables
