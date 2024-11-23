###########3##########
datos = [
    ["1", "Ángela", "Vargas", "1192743646", "Carrera 10A #30-24", "3046584196"],
    ["2", "Daniel", "Rueda", "1022922313", "Carerra 46 #35a 52", "3227619958"],
    ["3", "Juan", "Cerinza", "11111111", "Carerra 46 #35a 52", "33227619959"]
]
def bdatos(base):
    print(f"{'ID':<5} {'Nombre':<10} {'Apellido':<10} {'Documento':<12} {'Dirección':<30} {'Teléfono':<12}")
    print("="*85)
    for persona in base:
        id_persona, nombre, apellido, documento, direccion, telefono = persona
        print(f"{id_persona:<5} {nombre:<10} {apellido:<10} {documento:<12} {direccion:<30} {telefono:<12}")
bdatos(datos)
