import csv
from datetime import datetime, timedelta

class Libro:
    def __init__(self, codigo, autor, tema, num_paginas, cantidad, precio):
        self.codigo = codigo
        self.autor = autor
        self.tema = tema
        self.num_paginas = num_paginas
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return (f"Libro(codigo={self.codigo}, autor={self.autor}, tema={self.tema}, "
                f"num_paginas={self.num_paginas}, cantidad={self.cantidad}, precio={self.precio})")

class Usuario:
    def __init__(self, nombre, apellido, clave, rol="usuario"):
        self.nombre = nombre
        self.apellido = apellido
        self.__clave = clave
        self.rol = rol
        self.libros_prestados = []
        self.multas = 0

    def reservar_libro(self, libro):
        if libro.cantidad > 0:
            libro.cantidad -= 1
            fecha_prestamo = datetime.now()
            fecha_entrega = fecha_prestamo + timedelta(days=15)
            self.libros_prestados.append((libro, fecha_prestamo, fecha_entrega))
            print(f"{self.nombre} {self.apellido} ha reservado el libro: {libro.codigo}")
        else:
            print("No hay ejemplares disponibles.")

    def devolver_libro(self, codigo_libro):
        for prestamo in self.libros_prestados:
            libro, fecha_prestamo, fecha_entrega = prestamo
            if libro.codigo == codigo_libro:
                if datetime.now() > fecha_entrega:
                    dias_retraso = (datetime.now() - fecha_entrega).days
                    self.multas += dias_retraso * 2  # Multa de $2 por día de retraso
                libro.cantidad += 1
                self.libros_prestados.remove(prestamo)
                print(f"{self.nombre} {self.apellido} ha devuelto el libro: {libro.codigo}")
                return
        print("Este libro no está registrado como prestado.")

    def consultar_libros(self):
        for libro, fecha_prestamo, fecha_entrega in self.libros_prestados:
            print(f"Libro: {libro.codigo}, Fecha de entrega: {fecha_entrega.strftime('%Y-%m-%d')}")

    def consultar_multa(self):
        print(f"Multas pendientes: ${self.multas}")


class Administrador(Usuario):
    def crear_libro(self, codigo, autor, tema, num_paginas, cantidad, precio):
        return Libro(codigo, autor, tema, num_paginas, cantidad, precio)

    def editar_libro(self, libro, **kwargs):
        for key, value in kwargs.items():
            if hasattr(libro, key):
                setattr(libro, key, value)
        print(f"Libro {libro.codigo} actualizado.")

    def eliminar_libro(self, codigo_libro, lista_libros):
        for libro in lista_libros:
            if libro.codigo == codigo_libro:
                lista_libros.remove(libro)
                print(f"Libro {libro.codigo} eliminado.")
                return
        print("Libro no encontrado en el inventario.")

    def consultar_usuarios(self, usuarios):
        for usuario in usuarios:
            print(f"Usuario: {usuario.nombre} {usuario.apellido}, "
                  f"Libros prestados: {len(usuario.libros_prestados)}, Multa: ${usuario.multas}")
            usuario.consultar_libros()


def cargar_datos_csv():
    libros = []
    usuarios = []
    try:
        with open('libros.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                codigo, autor, tema, num_paginas, cantidad, precio = row
                libros.append(Libro(codigo, autor, tema, int(num_paginas), int(cantidad), float(precio)))
    except FileNotFoundError:
        pass

    try:
        with open('usuarios.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                nombre, apellido, clave, rol = row
                if rol == "administrador":
                    usuarios.append(Administrador(nombre, apellido, clave, rol))
                else:
                    usuarios.append(Usuario(nombre, apellido, clave, rol))
    except FileNotFoundError:
        pass

    return libros, usuarios


def guardar_usuario_csv(usuario):
    with open('usuarios.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([usuario.nombre, usuario.apellido, usuario._Usuario__clave, usuario.rol])
    print(f"Usuario {usuario.nombre} {usuario.apellido} registrado exitosamente.")

# Nueva función para guardar libros en el archivo CSV
def guardar_libro_csv(libro):
    with open('libros.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([libro.codigo, libro.autor, libro.tema, libro.num_paginas, libro.cantidad, libro.precio])
    print(f"Libro {libro.codigo} guardado en libros.csv")

def autenticar_usuario(nombre, clave, usuarios):
    for usuario in usuarios:
        if usuario.nombre == nombre and usuario._Usuario__clave == clave:
            return usuario
    return None


def menu_principal():
    libros, usuarios = cargar_datos_csv()

    while True:
        print("\nBienvenido a la Biblioteca UIS Barbosa\n")
        print("1. Iniciar Sesión")
        print("2. Registrarse")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            clave = input("Clave: ")
            usuario = autenticar_usuario(nombre, clave, usuarios)

            if usuario:
                if usuario.rol == "administrador":
                    while True:
                        print("\n--- Menú Administrador ---")
                        print("1. Agregar libro")
                        print("2. Editar libro")
                        print("3. Eliminar libro")
                        print("4. Consultar usuarios y préstamos")
                        print("5. Salir")
                        opcion_admin = input("Seleccione una opción: ")

                        if opcion_admin == "1":
                            codigo = input("Código del libro: ")
                            autor = input("Autor: ")
                            tema = input("Tema: ")
                            num_paginas = int(input("Número de páginas: "))
                            cantidad = int(input("Cantidad de ejemplares: "))
                            precio = float(input("Precio: "))
                            nuevo_libro = usuario.crear_libro(codigo, autor, tema, num_paginas, cantidad, precio)
                            libros.append(nuevo_libro)
                            guardar_libro_csv(nuevo_libro)

                        elif opcion_admin == "2":
                            codigo = input("Ingrese el código del libro a editar: ")
                            for libro in libros:
                                if libro.codigo == codigo:
                                    cantidad = int(input("Nueva cantidad: "))
                                    precio = float(input("Nuevo precio: "))
                                    usuario.editar_libro(libro, cantidad=cantidad, precio=precio)
                                    break
                            else:
                                print("Libro no encontrado.")

                        elif opcion_admin == "3":
                            codigo = input("Ingrese el código del libro a eliminar: ")
                            usuario.eliminar_libro(codigo, libros)

                        elif opcion_admin == "4":
                            usuario.consultar_usuarios(usuarios)

                        elif opcion_admin == "5":
                            print("Cerrando sesión de administrador.")
                            break

                        else:
                            print("Opción inválida, intente nuevamente.")

                else:
                    while True:
                        print("\n--- Menú Usuario ---")
                        print("1. Reservar libro")
                        print("2. Devolver libro")
                        print("3. Consultar libros prestados")
                        print("4. Consultar multas pendientes")
                        print("5. Salir")
                        opcion_usuario = input("Seleccione una opción: ")

                        if opcion_usuario == "1":
                            codigo = input("Ingrese el código del libro a reservar: ")
                            for libro in libros:
                                if libro.codigo == codigo:
                                    usuario.reservar_libro(libro)
                                    break
                            else:
                                print("Libro no encontrado.")

                        elif opcion_usuario == "2":
                            codigo = input("Ingrese el código del libro a devolver: ")
                            usuario.devolver_libro(codigo)

                        elif opcion_usuario == "3":
                            usuario.consultar_libros()

                        elif opcion_usuario == "4":
                            usuario.consultar_multa()

                        elif opcion_usuario == "5":
                            print("Cerrando sesión de usuario.")
                            break

                        else:
                            print("Opción inválida, intente nuevamente.")
            else:
                print("Credenciales incorrectas. Intente nuevamente.")

        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            clave = input("Clave: ")
            rol = input("Rol (usuario/administrador): ").lower()
            if rol == "administrador":
                nuevo_usuario = Administrador(nombre, apellido, clave, rol)
            else:
                nuevo_usuario = Usuario(nombre, apellido, clave, rol)
            usuarios.append(nuevo_usuario)
            guardar_usuario_csv(nuevo_usuario)

        elif opcion == "3":
            print("Gracias por usar el sistema de la Biblioteca UIS Barbosa. Hasta luego!")
            break

        else:
            print("Opción inválida.")

menu_principal()
