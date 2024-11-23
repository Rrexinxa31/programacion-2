def menu():
    id_seleccion = input("Ingrese el ID de la persona que desea editar: ")
    persona_encontrada = None
    for persona in datos:
        if persona[0] == id_seleccion:
            persona_encontrada = persona
            break
    
    if not persona_encontrada:
        print("ID no encontrado.")
        return
    
    seleccion = int(input("""Ingrese la opción de la acción que desea realizar:  
    1: Editar nombre
    2: Editar apellido
    3: Editar número de identidad
    4: Editar dirección
    5: Editar número de teléfono
    """))

    if seleccion == 1:
        nuevnombre = input("Ingrese el nuevo nombre: ")
        persona_encontrada[1] = nuevnombre
        print("Nombre actualizado.")
    elif seleccion == 2:
        nuevapellido = input("Ingrese el nuevo apellido: ")
        persona_encontrada[2] = nuevapellido
        print("Apellido actualizado.")
    elif seleccion == 3:
        nuevnum = input("Ingrese el nuevo número de identidad: ")
        persona_encontrada[3] = nuevnum
        print("Número de identidad actualizado.")
    elif seleccion == 4:
        nuevadi = input("Ingrese la nueva dirección: ")
        persona_encontrada[4] = nuevadi
        print("Dirección actualizada.")
    elif seleccion == 5:
        nuevtel = input("Ingrese el nuevo número de teléfono: ")
        persona_encontrada[5] = nuevtel
        print("Número de teléfono actualizado.")
    else:
        print("Opción no válida.")
    bdatos(datos)
menu()
