productos = []

def añadir_producto():
    nombre = input("Por favor ingrese el nombre del producto: ")
    while True:
        try:
            precio = float(input("Por favor ingrese el precio del producto: "))
            break
        except ValueError:
            print("Error: El precio debe ser un número.")

    while True:
        try:
            cantidad = int(input("Por favor ingrese la cantidad: "))
            break
        except ValueError:
            print("Error: La cantidad debe ser un número entero.")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(producto)
    print(f"Producto '{nombre}' agregado al inventario.")

def ver_productos():
    # Mostrar todos los productos
    print("Inventario actual:")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")

def actualizar_producto():
    ver_productos()
    try:
        indice = int(input("Ingrese el número del producto que desea actualizar: ")) - 1
        if 0 <= indice < len(productos):
            productos[indice]['nombre'] = input("Nuevo nombre del producto: ")

            # Solicitar nuevo precio hasta que el usuario ingrese un valor válido
            while True:
                try:
                    productos[indice]['precio'] = float(input("Nuevo precio del producto: "))
                    break
                except ValueError:
                    print("Error: El precio debe ser un número.")

            # Solicitar nueva cantidad hasta que el usuario ingrese un valor válido
            while True:
                try:
                    productos[indice]['cantidad'] = int(input("Nueva cantidad del producto: "))
                    break
                except ValueError:
                    print("Error: La cantidad debe ser un número entero.")

            print("Producto actualizado.")
        else:
            print("Índice de producto no válido.")
    except ValueError:
        print("Error: Por favor ingrese un número válido para el índice.")

def eliminar_producto():
    ver_productos()
    try:
        indice = int(input("Ingrese el número del producto que desea eliminar: ")) - 1
        if 0 <= indice < len(productos):
            eliminado = productos.pop(indice)
            print(f"Producto '{eliminado['nombre']}' eliminado del inventario.")
        else:
            print("Índice de producto no válido.")
    except ValueError:
        print("Error: Por favor ingrese un número válido para el índice.")

def guardar_datos():
    # Guardar los datos en un archivo de texto
    with open("inventario.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Datos guardados correctamente.")

def cargar_datos():
    try:
        with open("inventario.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')
                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                }
                productos.append(producto)
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró un archivo de inventario previo.")
    except ValueError:
        print("Error al leer los datos del archivo. Revisa el formato del archivo.")

def menu():
    cargar_datos()  # Cargar los datos al inicio del programa
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

menu()

