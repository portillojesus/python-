productos = []

def añadir_producto():
    nombre = input("Por favor ingrese el nombre del producto: ")
    precio = float(input("Por favor ingrese el precio del producto: "))
    cantidad = input("Por favor ingrese la cantidad: ")

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
    # Actualizar un producto existente
    ver_productos()
    indice = int(input("Ingrese el número del producto que desea actualizar: ")) - 1
    if 0 <= indice < len(productos):
        productos[indice]['nombre'] = input("Nuevo nombre del producto: ")
        productos[indice]['precio'] = float(input("Nuevo precio del producto: "))
        productos[indice]['cantidad'] = input("Nueva cantidad del producto: ")
        print("Producto actualizado.")
    else:
        print("Índice de producto no válido.")

def eliminar_producto():
    # Eliminar un producto
    ver_productos()
    indice = int(input("Ingrese el número del producto que desea eliminar: ")) - 1
    if 0 <= indice < len(productos):
        eliminado = productos.pop(indice)
        print(f"Producto '{eliminado['nombre']}' eliminado del inventario.")
    else:
        print("Índice de producto no válido.")

def guardar_datos():
    # Guardar los datos en un archivo de texto
    with open("inventario.txt", "w") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)
    print("Datos guardados correctamente.")

def cargar_datos():
    # Cargar los datos desde un archivo de texto
    try:
        with open("inventario.txt", "r") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(',')
                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": cantidad
                }
                productos.append(producto)
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró un archivo de inventario previo.")

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

