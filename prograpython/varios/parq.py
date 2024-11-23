import datetime as dt
rc=0
rm=0
rcc=[]
rmm=[]
rt=[rcc,rmm]

def menu():
    b=input("""Bienvenido al parqueadero cerinza
          1.entrada
          2.salida
          """)
    if b == "1":
        global rc
        global tp   
        tp=input("""Ingrese tipo de vehiculo carro o moto
        1.carro
        2.moto
        """)
        rc += 1
    else:
        global rm
        tp=input("""Ingrese tipo de vehiculo carro o moto
        1.carro
        2.moto
        """)
        rm += 1
     
    if tp == "1":
        
        rplaca=input("ingrese la placa del vehiculo porfavor")
        rcc.append(rplaca)
    else:
        rplaca=input("ingrese la placa del vehiculo porfavor")
        rmm.append(rplaca)

            
            
        
            
menu()
