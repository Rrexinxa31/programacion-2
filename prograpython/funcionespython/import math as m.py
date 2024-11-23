import math as m
radio=float(input("Ingrese radio"))
def area_perimetro_circulo(radio):
    peri=2*m.pi*radio
    area=m.pi*(radio)**2
    return peri, area
peri,area=area_perimetro_circulo(radio)
print("Perimetro= ", peri , "Area= ", area)