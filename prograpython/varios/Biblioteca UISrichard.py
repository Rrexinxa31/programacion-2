import os
import pandas as pd
from datetime import datetime, timedelta

# Archivos CSV
archivo_libros = "libros.csv"
archivo_usuarios = "usuarios.csv"

# Inicialización de DataFrames
if os.path.exists(archivo_libros):
    df_libros = pd.read_csv(archivo_libros)
else:
    df_libros = pd.DataFrame(columns=["numero_inventario", "autor", "tema", "num_paginas", "cantidad", "precio"])

if os.path.exists(archivo_usuarios):
    df_usuarios = pd.read_csv(archivo_usuarios)
else:
    df_usuarios = pd.DataFrame(columns=["nombre", "apellido", "clave", "prestamos"])

class Libro:
    def __init__(self, numero_inventario, autor, tema, num_paginas, cantidad, precio):
        self.numero_inventario = numero_inventario
        self.autor = autor
        self.tema = tema
        self.num_paginas = num_paginas
        self.cantidad = cantidad
        self.precio = precio

class Usuario:
    def __init__(self, nombre, apellido, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.__clave = clave
        self.prestamos = []

    def verificar_clave(self, clave):
        return self.__clave == clave

class Administrador(Usuario):
    def agregar_libro(self, libro):
        global df_libros
        df_libros = df_libros._append({
            "numero_inventario": libro.numero_inventario,
            "autor": libro.autor,
            "tema": libro.tema,
            "num_paginas": libro.num_paginas,
            "cantidad": libro.cantidad,
            "precio": libro.precio
        }, ignore_index=True)
        df_libros.to_csv(archivo_libros, index=False)
        print(f"Libro '{libro.numero_inventario}' agregado con éxito y guardado en el archivo.")

    def crear_usuario(self, nombre, apellido, clave):
        global df_usuarios
        df_usuarios = df_usuarios._append({
            "nombre": nombre,
            "apellido": apellido,
            "clave": clave,
            "prestamos": ""
        }, ignore_index=True)
        df_usuarios.to_csv(archivo_usuarios, index=False)
        print(f"Usuario '{nombre} {apellido}' creado con éxito y guardado en el archivo.")

    def ver_prestamos_y_deudas(self):
        usuarios_con_prestamos = df_usuarios[df_usuarios['prestamos'].notna() & (df_usuarios['prestamos'] != "")]
        
        if usuarios_con_prestamos.empty:
            print("No hay usuarios con préstamos activos.")
            return
        
        for _, row in usuarios_con_prestamos.iterrows():
            nombre = row['nombre']
            apellido = row['apellido']
            prestamos = row['prestamos'].split(';') if isinstance(row['prestamos'], str) else []
            deudas = False
            print(f"\nUsuario: {nombre} {apellido}")
            for prestamo in prestamos:
                numero_inventario, fecha_entrega = prestamo.split(" - Entrega: ")
                fecha_entrega = datetime.strptime(fecha_entrega, '%Y-%m-%d')
                if fecha_entrega < datetime.now():
                    print(f" - {numero_inventario}: Vencido (deuda)")
                    deudas = True
                else:
                    print(f" - {numero_inventario}: Activo (Fecha de entrega: {fecha_entrega.strftime('%Y-%m-%d')})")
        if not deudas:
            print(" - Sin deudas.")
        print("\n--------------------------------")


def menu_administrador(admin):
    while True:
        print("\n--- Menú Administrador ---")
        print("1. Agregar Libro")
        print("2. Crear Usuario")
        print("3. Ver Usuarios con Préstamos y Deudas")
        print("4. Salir al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_inventario = input("Número de inventario: ")
            autor = input("Autor: ")
            tema = input("Tema: ")
            num_paginas = int(input("Número de páginas: "))
            cantidad = int(input("Cantidad de ejemplares: "))
            precio = float(input("Precio de compra: "))
            libro = Libro(numero_inventario, autor, tema, num_paginas, cantidad, precio)
            admin.agregar_libro(libro)
        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            clave = input("Clave: ")
            admin.crear_usuario(nombre, apellido, clave)
        elif opcion == "3":
            admin.ver_prestamos_y_deudas()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
class UsuarioBiblioteca(Usuario):
    def reservar_libro(self, numero_inventario):
        global df_libros, df_usuarios
        libro = df_libros[df_libros['numero_inventario'] == numero_inventario]
        if not libro.empty and libro.iloc[0]['cantidad'] > 0:
            df_libros.loc[df_libros['numero_inventario'] == numero_inventario, 'cantidad'] -= 1
            fecha_entrega = calcular_fecha_entrega().strftime('%Y-%m-%d')
            prestamo_info = f"{numero_inventario} - Entrega: {fecha_entrega}"
            self.prestamos.append(prestamo_info)
            prestamos_actualizados = ';'.join(self.prestamos)
            df_usuarios.loc[(df_usuarios['nombre'] == self.nombre) & (df_usuarios['apellido'] == self.apellido), 'prestamos'] = prestamos_actualizados
            df_libros.to_csv(archivo_libros, index=False)
            df_usuarios.to_csv(archivo_usuarios, index=False)
            print(f"Libro reservado exitosamente. Fecha de entrega: {fecha_entrega}")
        else:
            print("Libro no disponible para préstamo.")

    def ver_prestamos_y_multa(self):
        if self.prestamos:
            print("Préstamos activos y fechas de entrega:")
            for prestamo in self.prestamos:
                print(prestamo)
        else:
            print("No tiene préstamos activos.")

def calcular_fecha_entrega():
    return datetime.now() + timedelta(days=15)

# Resto del código para menú principal e interacción con el usuario

def menu_usuario(usuario):
    while True:
        print("\n--- Menú Usuario ---")
        print("1. Reservar Libro")
        print("2. Ver Préstamos y Multas")
        print("3. Salir al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_inventario = input("Número de inventario del libro a reservar: ")
            usuario.reservar_libro(numero_inventario)
        elif opcion == "2":
            usuario.ver_prestamos_y_multa()
        elif opcion == "3":
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Instanciamos el administrador y el usuario para simular el sistema
admin = Administrador("Admin", "Principal", "1234")
usuario = UsuarioBiblioteca("Juan", "Perez", "claveSegura")

# Menú Principal
while True:
    print("\n--- Menú Principal ---")
    print("1. Ingresar como Administrador")
    print("2. Ingresar como Usuario")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        clave = input("Ingrese la clave de administrador: ")
        if admin.verificar_clave(clave):
            menu_administrador(admin)
        else:
            print("Clave incorrecta.")
    elif opcion == "2":
        menu_usuario(usuario)
    elif opcion == "3":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
