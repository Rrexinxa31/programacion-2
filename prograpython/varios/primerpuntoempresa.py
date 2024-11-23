import csv
from datetime import datetime

class Producto:
    def __init__(self, JDRC_nombre, JDRC_precio, JDRC_cantidad_stock):
        self.JDRC_nombre = JDRC_nombre
        self._JDRC_precio = JDRC_precio  # Precio encapsulado
        self.JDRC_cantidad_stock = JDRC_cantidad_stock

    def actualizar_stock(self, JDRC_cantidad):
        if JDRC_cantidad <= self.JDRC_cantidad_stock:
            self.JDRC_cantidad_stock -= JDRC_cantidad
            return True
        return False

    def mostrar_info(self):
        return f"{self.JDRC_nombre} - Precio: {self._JDRC_precio} - Stock: {self.JDRC_cantidad_stock}"

class Electronico(Producto):
    def __init__(self, JDRC_nombre, JDRC_precio, JDRC_cantidad_stock, JDRC_garantia):
        super().__init__(JDRC_nombre, JDRC_precio, JDRC_cantidad_stock)
        self.JDRC_garantia = JDRC_garantia

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Garantía: {self.JDRC_garantia} meses"

class Alimento(Producto):
    def __init__(self, JDRC_nombre, JDRC_precio, JDRC_cantidad_stock, JDRC_fecha_vencimiento):
        super().__init__(JDRC_nombre, JDRC_precio, JDRC_cantidad_stock)
        self.JDRC_fecha_vencimiento = JDRC_fecha_vencimiento

    def mostrar_info(self):
        return f"{super().mostrar_info()} - Fecha de vencimiento: {self.JDRC_fecha_vencimiento}"

class Inventario:
    def __init__(self):
        self.JDRC_lista_productos = []

    def agregar_producto(self, JDRC_producto):
        self.JDRC_lista_productos.append(JDRC_producto)

    def mostrar_productos(self):
        for JDRC_producto in self.JDRC_lista_productos:
            print(JDRC_producto.mostrar_info())

    def realizar_venta(self, JDRC_nombre_producto, JDRC_cantidad):
        for JDRC_producto in self.JDRC_lista_productos:
            if JDRC_producto.JDRC_nombre == JDRC_nombre_producto:
                if JDRC_producto.actualizar_stock(JDRC_cantidad):
                    print("Venta realizada con éxito.")
                else:
                    print("Stock insuficiente.")
                return
        print("Producto no encontrado.")

    def guardar_csv(self, JDRC_archivo):
        with open(JDRC_archivo, mode='w', newline='') as JDRC_file:
            JDRC_writer = csv.writer(JDRC_file)
            JDRC_writer.writerow(["nombre", "precio", "cantidad_stock", "tipo", "extra"])
            for JDRC_producto in self.JDRC_lista_productos:
                JDRC_tipo = "Electronico" if isinstance(JDRC_producto, Electronico) else "Alimento"
                JDRC_extra = JDRC_producto.JDRC_garantia if JDRC_tipo == "Electronico" else JDRC_producto.JDRC_fecha_vencimiento
                JDRC_writer.writerow([JDRC_producto.JDRC_nombre, JDRC_producto._JDRC_precio, 
                                      JDRC_producto.JDRC_cantidad_stock, JDRC_tipo, JDRC_extra])

    def cargar_csv(self, JDRC_archivo):
        with open(JDRC_archivo, mode='r') as JDRC_file:
            JDRC_reader = csv.DictReader(JDRC_file)
            for JDRC_row in JDRC_reader:
                if JDRC_row["tipo"] == "Electronico":
                    JDRC_producto = Electronico(JDRC_row["nombre"], float(JDRC_row["precio"]), 
                                                int(JDRC_row["cantidad_stock"]), int(JDRC_row["extra"]))
                else:
                    JDRC_producto = Alimento(JDRC_row["nombre"], float(JDRC_row["precio"]), 
                                             int(JDRC_row["cantidad_stock"]), JDRC_row["extra"])
                self.agregar_producto(JDRC_producto)

def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Mostrar stock")
    print("2. Vender productos")
    print("3. Agregar producto")
    print("4. Salir")
    JDRC_opcion = input("Seleccione una opción: ")
    return JDRC_opcion

def agregar_producto(JDRC_inventario):
    JDRC_tipo = input("Ingrese el tipo de producto (Electronico/Alimento): ").strip().lower()
    JDRC_nombre = input("Nombre del producto: ")
    JDRC_precio = float(input("Precio del producto: "))
    JDRC_cantidad_stock = int(input("Cantidad en stock: "))

    if JDRC_tipo == "electronico":
        JDRC_garantia = int(input("Garantía (en meses): "))
        JDRC_producto = Electronico(JDRC_nombre, JDRC_precio, JDRC_cantidad_stock, JDRC_garantia)
    elif JDRC_tipo == "alimento":
        JDRC_fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
        JDRC_producto = Alimento(JDRC_nombre, JDRC_precio, JDRC_cantidad_stock, JDRC_fecha_vencimiento)
    else:
        print("Tipo de producto no válido.")
        return

    JDRC_inventario.agregar_producto(JDRC_producto)
    print("Producto agregado con éxito.")

def vender_producto(JDRC_inventario):
    JDRC_nombre_producto = input("Nombre del producto a vender: ")
    JDRC_cantidad = int(input("Cantidad a vender: "))
    JDRC_inventario.realizar_venta(JDRC_nombre_producto, JDRC_cantidad)

def main():
    JDRC_inventario = Inventario()
    JDRC_inventario.cargar_csv("inventario.csv")

    while True:
        JDRC_opcion = mostrar_menu()
        if JDRC_opcion == "1":
            JDRC_inventario.mostrar_productos()
        elif JDRC_opcion == "2":
            vender_producto(JDRC_inventario)
        elif JDRC_opcion == "3":
            agregar_producto(JDRC_inventario)
        elif JDRC_opcion == "4":
            JDRC_inventario.guardar_csv("inventario.csv")
            print("Guardando inventario y saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
