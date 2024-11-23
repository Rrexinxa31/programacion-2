positivos=0

negativos=0

contp=0
for i in range(5):
    n=int(input("Ingrese un numero "))
    if n<0:
        negativos+=n
        
    elif n>0:
        positivos+=n
        contp += 1
        
print("La sumatoria de los números negativos es ",negativos)

if positivos>0:
    
    prom = positivos / contp
    print("El promedio de los números positivos es ",prom)
    
else:
    
    print("No se ingresaron números positivos")
