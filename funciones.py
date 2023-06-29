import os
import json

def clear_console():
    os.system('clear' if os.name == 'posix' else 'cls')

def cargar():
    try:
        with open('insumos.json', 'r') as arcInsumos:
            insumos = json.load(arcInsumos)
    except FileNotFoundError:
        insumos = []
    return insumos

def guardar(insumos):
    with open('insumos.json', 'w') as arcInsumos:
        json.dump(insumos, arcInsumos, indent=4)

def mostrarInsumos():
    print("||   LISTADO DE INSUMOS   ||")
    print("----------------------------")
    print(" ")
    insumos = cargar()
    if insumos:
        for insumo in insumos:
            print("Categoria:", insumo["categoria"])
            print("Item:", insumo["item"])
            print("Cantidad:", insumo["cantidad"])
            print("----------------------------------------")
    else:
        print("No hay insumos almacenados.")

def agregarInsumo():
     while True:
        clear_console()
        print("--- Insumos: Categorias ---")
        print("1. Maltas")
        print("2. Levaduras")
        print("3. Lupulos")
        print("4. Adicionales")
        print("5. Clarificantes")
        print("6. Otros")
        print("7. Retornar al menu principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clear_console()
            print("Maltas...")
            item = input("Ingrese el nombre del insumo: ")
            cantidad = input("Ingrese la cantidad de insumo adquirida (kg): ")
            precio = input("Ingrese el precio del insumo: ")
            fechacom = input("Ingrese la fecha de la compra: ")
            provehedor = input("Ingrese el proveedor: ")
            nuevoMalta = {
                "item": item,
                "cantidad": cantidad,
                "precio": precio,
                "fechacom": fechacom,
                "provehedor": provehedor,
                "categoria": "Maltas" }
            maltas = cargar()
            maltas.append(nuevoMalta)
            guardar(maltas)

            print("El insumo ha sido cargado exitosamente.")
            input("Presione Enter para continuar...")
        elif opcion == "2":
            clear_console()
            print("Levaduras...")
            item = input("Ingrese el nombre del insumo: ")
            cantidad = input("Ingrese la cantidad de insumo adquirida (sobres): ")
            precio = input("Ingrese el precio del insumo: ")
            fechacom = input("Ingrese la fecha de la compra: ")
            provehedor = input("Ingrese el proveedor: ")
            nuevoLeva = {
                "item": item,
                "cantidad": cantidad,
                "precio": precio,
                "fechacom": fechacom,
                "provehedor": provehedor,
                "categoria": "Levaduras"}
            levaduras = cargar()
            levaduras.append(nuevoLeva)
            guardar(levaduras)

            print("El insumo ha sido cargado exitosamente.")
            input("Presione Enter para continuar...")
        elif opcion == "3":
            nuevaCompra()
        elif opcion == "4":
            eliminarInsumo()
        elif opcion == "7":
            break
            menu()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
############################################################################
def nuevaCompra():
    item = input("Ingrese el item del insumo adquirido: ")

    insumos = cargar()
    indice = None

    for i, componente in enumerate(insumos):
        if componente["item"] == item:
            indice = i
            break

    if indice is not None:
        nuevoCant = input("Ingrese la cantidad adquirida: ")
        nuevoPrecio = input("Ingrese el precio del insumo: ")
        nuevoFechacom = input("Ingrese la fecha de la nueva compra: ")
        nuevoProve = input("Ingrese el proveedor de la compra: ")

        insumo_existente = insumos[indice]
        categoria = insumo_existente["categoria"]
        cantidad_existente = int(insumo_existente["cantidad"])
        nueva_cantidad = int(nuevoCant)

        if categoria == "Maltas" or categoria == "Levaduras":
            insumos[indice]["cantidad"] = str(cantidad_existente + nueva_cantidad)
        else:
            insumos[indice]["cantidad"] = nuevoCant

        insumos[indice]["precio"] = nuevoPrecio
        insumos[indice]["fechacom"] = nuevoFechacom
        insumos[indice]["nuevoProve"] = nuevoProve

        guardar(insumos)
        print("Actualización por la nueva compra exitosa.")
        input("Presione Enter para continuar...")
    else:
        print("No existe el insumo. Agréguelo")
        input("Presione Enter para continuar...")

###################################################################
def eliminarInsumo():
    item = input("Ingrese el item del insumo que desea eliminar: ")

    insumos = cargar()
    indice = None

    for i, componente in enumerate(insumos):
        if componente["item"] == item:
            indice = i
            break

    if indice is not None:
        del insumos[indice]
        guardar(insumos)
        print("Se ha eliminado exitosamente el insumo", item + ".")
        input("Presione Enter para continuar...")
    else:
        print("No se ha encontrado el insumo especificado.")
        input("Presione Enter para continuar...")

def menu():
    while True:
        clear_console()

        print("----- Cerveceria LosInge -----")
        print("1. Mostrar stock de insumos")
        print("2. Agregar nuevo insumo")
        print("3. Cargar insumo de nueva compra")
        print("4. Eliminar insumo")
        print("5. Exit")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clear_console()
            mostrarInsumos()
            input("Presione Enter para continuar...")
        elif opcion == "2":
            clear_console()
            agregarInsumo()
        elif opcion == "3":
            clear_console()
            nuevaCompra()
        elif opcion == "4":
            clear_console()
            eliminarInsumo()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            input("Presione Enter para continuar...")

menu()
