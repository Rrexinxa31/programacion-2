#11

import math

def area_perimetro_circulo(radio):
    perimetro = math.pi*(radio+radio)
    area = math.pi*radio**2
    return perimetro,area
ra = float(input("porfavor ingrese el radio del circulo "))
perimetro,area = area_perimetro_circulo(ra)
print("perimetro : ",round(perimetro,2)," area : ",round(area,2))
