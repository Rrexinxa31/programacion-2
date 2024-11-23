base=int(input("ingrese base"))
altura=int(input("ingrese altura"))
def area_perimetro_rectangulo(base, altura):
    peri=2*(base + altura)
    area=(base*altura)/2
    return peri, area
peri, area= area_perimetro_rectangulo(base, altura)
print("Area= ", area, "Perimetro= ", peri )