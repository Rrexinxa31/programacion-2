############ejercisios aplicaciones####################
datos = [
    ("Ángela", "Vargas", "1192743646", "Carrera 10A #30-24", "3046584196"),
    ("Daniel", "Rueda", "1022922313", "carrera 46 #35a 52", "3227619958"),
    ("Juan", "Cerinza", "1022922313", "carrera 46 #35a 52", "3227619959")
]
def bdatos(base):
    print(f"{'Nombre':<10} {'Apellido':<10} {'Documento':<12} {'Dirección':<30} {'Teléfono':<12}")
    print("="*75)
    for persona in base:
        nombre, apellido, documento, direccion, telefono = persona
        print(f"{nombre:<10} {apellido:<10} {documento:<12} {direccion:<30} {telefono:<12}")

bdatos(datos)
