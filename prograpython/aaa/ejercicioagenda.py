import pandas as pd

import re

class Contacto:
    def __init__(self, J, D, R):
        self.J = J  # nombre
        self.D = D  # teléfono
        if self.validar_R(R):
            self.R = R  # correo
        else:
            raise ValueError("Correo electrónico no válido")

    def validar_R(self, R):
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(patron, R)

class Agenda:
    def __init__(self, C="C:\Users\sadad\OneDrive\Desktop\aaa"):
        self.C = C  # archivo_csv
        try:
            self.contactos = pd.read_csv(self.C)
        except FileNotFoundError:
            self.contactos = pd.DataFrame(columns=['Nombre', 'Teléfono', 'Correo'])
    
    def añadir_contacto(self, J, D, R):
        try:
            contacto = Contacto(J, D, R)
            nuevo_contacto = {'Nombre': contacto.J, 'Teléfono': contacto.D, 'Correo': contacto.R}
            self.contactos = self.contactos.append(nuevo_contacto, ignore_index=True)
            self.guardar()
            print(f"Contacto {J} añadido correctamente.")
        except ValueError as e:
            print(e)
    
    def lista_contactos(self):
        if not self.contactos.empty:
            print(self.contactos)
        else:
            print("No hay contactos guardados.")
    
    def buscar_contacto(self, J):
        contacto = self.contactos[self.contactos['Nombre'].str.contains(J, case=False, na=False)]
        if not contacto.empty:
            print(contacto)
        else:
            print(f"No se encontraron contactos con el nombre: {J}")
    
    def editar_contacto(self, J):
        indice = self.contactos[self.contactos['Nombre'].str.contains(J, case=False, na=False)].index
        if not indice.empty:
            print(f"Editando el contacto {J}. Deja vacío si no deseas cambiar.")
            nuevo_J = input("Nuevo nombre: ").strip() or self.contactos.at[indice[0], 'Nombre']
            nuevo_D = input("Nuevo teléfono: ").strip() or self.contactos.at[indice[0], 'Teléfono']
            nuevo_R = input("Nuevo correo: ").strip()
            if nuevo_R and not Contacto.validar_R(None, nuevo_R):
                print("Correo electrónico no válido.")
            else:
                self.contactos.at[indice[0], 'Nombre'] = nuevo_J
                self.contactos.at[indice[0], 'Teléfono'] = nuevo_D
                if nuevo_R:
                    self.contactos.at[indice[0], 'Correo'] = nuevo_R
                self.guardar()
                print(f"Contacto {J} actualizado correctamente.")
        else:
            print(f"No se encontraron contactos con el nombre: {J}")
    
    def eliminar_contacto(self, J):
        indice = self.contactos[self.contactos['Nombre'].str.contains(J, case=False, na=False)].index
        if not indice.empty:
            self.contactos = self.contactos.drop(indice)
            self.guardar()
            print(f"Contacto {J} eliminado correctamente.")
        else:
            print(f"No se encontraron contactos con el nombre: {J}")
    
    def cerrar_agenda(self):
        print("Cerrando agenda...")
    
    def guardar(self):
        self.contactos.to_csv(self.C, index=False)

def menu():
    agenda = Agenda()
    
    while True:
        print("\n----- Menú de Agenda -----")
        print("1. Añadir contacto")
        print("2. Lista de contactos")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Eliminar contacto")
        print("6. Cerrar agenda")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            J = input("Nombre: ").strip()
            D = input("Teléfono: ").strip()
            R = input("Correo electrónico: ").strip()
            agenda.añadir_contacto(J, D, R)
        elif opcion == '2':
            agenda.lista_contactos()
        elif opcion == '3':
            J = input("Ingrese el nombre a buscar: ").strip()
            agenda.buscar_contacto(J)
        elif opcion == '4':
            J = input("Ingrese el nombre del contacto a editar: ").strip()
            agenda.editar_contacto(J)
        elif opcion == '5':
            J = input("Ingrese el nombre del contacto a eliminar: ").strip()
            agenda.eliminar_contacto(J)
        elif opcion == '6':
            agenda.cerrar_agenda()
            break
        else:
            print("Opción no válida, por favor intente nuevamente.")
menu()
