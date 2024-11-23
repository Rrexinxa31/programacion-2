import tkinter as tk
app=tk.Tk()
palabra = tk.StringVar(app)#almacena datos tipo cadena a nuestra ventana
entrada = tk.StringVar(app)


#dimensiones de la ventana anchoxalto
app.geometry("600x300")
app.configure(background="green") #el color de fondo
tk.Wm.wm_title(app,"Universidad Industrial de Santander =)") #titulo de la ventana hecha

def cambiarpalabra():#definimos una funcion para cambiar la label
    palabra.set("Hola ingeniero " + entrada.get())#.set para cambiar el valor y poenemos la variable entrada para recoger el dato ingresado
#crea un boton
tk.Button(
    app,#nombre de la ventana creada
    text="Holaaaa compañero UIS",#texto en el boton
    font=("Arial", 14),#tipo de letra o fuente y su tamaño
    bg="#DAF7A6",#color de fondo
    fg="white",#color de la fuente
    command=cambiarpalabra, #comando que hace el boton
    relief="flat",#estilo ddel borde del boton 
).pack(
    fill=tk.BOTH, #esto es para que el boton ocupe el espacio por igual
    expand=True, #esto es para que se expanda si hay algun cambio de tamaño
) #añade el boton a nuestra ventana 

tk.Label( #genera una ventana de texto
    app,#se agrega a nuestra ventana creada
    textvariable=palabra,#aqui es donde el valor que ingresemos se muestra en la ventana
    fg="black",#color de la fuente
    bg="#85EF0C",#color de fondo
    justify="center",#que el texto sea centrado
).pack(#empaquetamos esto a nuestra ventana
    fill=tk.BOTH,#ocupe espacio por igual
    expand=True,#esto es para que se expanda si hay algun cambio de tamaño
)

tk.Entry(#genera una ventana donde podemos ingresar datos
    app,#se agrega a nuestra ventana
    fg="black",#color de fuente
    bg="#85EF0C",#color de fondo
    justify="center",#ajusta el texto
    textvariable=entrada,#aqui se ingresa el dato
).pack(
    fill=tk.BOTH,
    expand=True,
)

app.mainloop() #refresca cualquier cambio en la ventana