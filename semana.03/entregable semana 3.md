


# 1 - Crear funcion para añadir producto
# Ahora vamos a hacer una función que reciba tres parámetros: nombre, precio y cantidad, y lo guarde en el diccionario inventario

    #   Validar que el nombre no esté ya en el inventario
    #   Asegurarse de que precio y cantidad sean válidos (números positivos)
    #   Manejar si el usuario pone algo incorrecto

def añadir_producto(inventario, nombre, precio, cantidad):
    if nombre in inventario:
        print("El producto ya existe en el inventario")
        return
    
    if not isinstance(precio, (int, float)) or precio <= 0:
        print("El precio debe ser un numero positivo. ")
        return 
    
    if not isinstance(cantidad, int) or cantidad < 0: 
        print("La cantidad debe ser un numero entero positivo o cero. ")
        return
    
    inventario[nombre] = (precio, cantidad)
    print(f"producto '{nombre}' añadido correctamente. ")



# 2 - Consultar producto por nombre 
# Esta función buscará un producto y mostrará su precio y cantidad. Si no existe, debe notificarlo.

def consultar_producto(inventario, nombre):
    if nombre in inventario:
        precio, cantidad = inventario[nombre]
        print(f"Producto: {nombre}")
        print(f"Precio: ${precio}")
        print(f"Cantidad disponible: {cantidad}")
    else: 
        print(f"El producto'{nombre}' no esta en el inventario. ")



# 3 - Actualizar el precio de un producto.

    #   Permitir al usuario cambiar el precio de un producto ya existente.
    #   Validar que el producto esté en el inventario.
    #   Validar que el nuevo precio sea válido (número positivo).

def actualizar_precio(inventario, nombre, nuevo_precio):
    if nombre not in inventario:
        print(f"El producto '{nombre}' no está en el inventario. ")
        return
    
    if not isinstance(nuevo_precio, (int, float)) or nuevo_precio <= 0: 
        print("EL nuevo precio debe ser un número positivo. ")
        return 
    
    cantidad = inventario[nombre][1]
    inventario[nombre] = (nuevo_precio, cantidad)
    print(f"Precio de '{nombre}' actualizado a ${nuevo_precio}. ")


# 4 - Eliminar productos del inventario.
# Eliminar un producto del inventario si existe. Si no existe, notificar al usuario.

def eliminar_producto(inventario, nombre):
    if nombre in inventario: 
        del inventario[nombre]
        print(f"Producto '{nombre}' ha sido eliminado del inventario. ")
    else:
        print(f"EL producto '{nombre}' no se encuentra en el inventario. ")


# 5 - Calcular el valor total del inventario usando una función lambda.
# Multiplicar el precio × cantidad de cada producto y sumar el total general del inventario.

def calcular_valor_total(inventario):
    valor_total = sum(map(lambda item: item[1][0] * item[1][1], inventario.items()))
    print(f"valor total del inventario: ${valor_total:.2f}")

# programa principal 

def menu():
    inventario = {}

    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Añadir producto. ")
        print("2. Consultar producto. ")
        print("3. Actualizar precio. ")
        print("4. ELiminar producto. ")
        print("5. Calcular Valor total de inventario. ")
        print("6. Salir. ")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            try:
                precio = float(input("Precio: "))
                cantidad = int(input("Cantidad: "))
            except ValueError:
                print("Precio y Cantidad deben ser números válidos. ")
                continue
            añadir_producto(inventario, nombre, precio, cantidad)

        elif opcion == "2":
            nombre = input("Nombre del producto a consultar: ")
            consultar_producto(inventario, nombre)

        elif opcion == "3": 
            nombre = input("Nombre del producto a actualizar: ")
            try:
                nuevo_precio = float(input("Nuevo precio: "))
            except ValueError:
                print("El precio debe ser un número válido. ")
                continue
            actualizar_precio(inventario, nombre, nuevo_precio)

        elif opcion == "4":
            nombre = input("NOmbre del producto a actualizar: ")
            eliminar_producto(inventario, nombre)

        elif opcion == "5":
            calcular_valor_total(inventario)

        elif opcion == "6": 
            print("Saliendo del programa... ")

        else: 
            print("Opción inválida. Por favor seleccione un numero del 1 al 6. ")

# ejecutar menu
menu()
