###########2##########
meses = ("enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","nomviembre","diciembre")

def mes():
    while True:
        number = int(input("ingrese un numero entre 1 y 12 o ingrese el 0 para salir del programa"))
        if number>=1 and number<=12:
            print("el mes correspondiente es :",{meses[number-1]})
        elif number==0:
            print("fin del programa")
            break
        else:
            print("dato ingresado erroneo")

mes()
