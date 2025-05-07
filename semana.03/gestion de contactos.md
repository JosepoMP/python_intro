# Ejercicio: Gestión de Contactos
# Objetivo:

# Crea una pequeña agenda en donde se guardara el nombre, el celular, estado civil, genero, todo esto se guardara dentro de un lista para que tengamos una lista de contactos

    # Agregar un nuevo contacto.
    # Buscar un contacto por su nombre o celular.
    # Mostrar todos los contactos.
    # Modificar un contacto en especifico
    # Eliminar un contacto.

# 📦 Requisitos

    # Usar un diccionario para guardar la informacion y dentro de una lista guarda todos estos contactos
    # plus: a la hora de eliminar o modificar que me mustre los contactos existentes para asi verificar cual quiero modificar

# 1 - Agregar contactos 

contactos = {}

def agregar_contacto():
    nombre = input("Introduce el nombre del contacto: ")
    if nombre in contactos:
        print("⚠️ Este contacto ya esta registrado. ")
        return 
    try:
        numero = int(input("Introduzca el numero telefonico del contacto: "))
    except ValueError:
        print("❌ Número inválido. Intenta de nuevo con solo dígitos.")
        return
    contactos[nombre] = {
        "numero": numero 
    }
    print(f"✅ ¡{nombre} ha sido registrado con éxito!.")


# 2 - Mostrar contactos almacenados 

def mostrar_contacto():
    if contactos:
        print("\n📒 Informacion de todos los contactos:\n")
        for nombre, datos in contactos.items():
            print(f"Nombre: {nombre}")
            print(f"Numero: {datos['numero']}")
            print("-" * 30)
    else: 
        print("📭 No hay contactos registrados. ")

# 3 - Modificar un contacto en especifico

def modificar_contacto():
    if not contactos: 
        print("📭 No hay contactos registrados aún.")
        return
    
    print("📋 Contactos registrados: ")
    for nombre in contactos:
        print(f"- {nombre}")

    nombre = input("Ingrese el nombre del contacto que desea modificar: ")

    if nombre not in contactos:
        print("❌ Ese contacto no está registrado.")
        return
    
    print("\n¿Que deseas modificar?")
    print("1. Nombre ")
    print("2. Número ")
    print("3. Ambos ")
    eleccion = input("Seleccione una opcion (1-3): ")

    if eleccion == "1":
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        contactos[nuevo_nombre] = contactos.pop(nombre)
        print(f"✅ Nombre actualizado: ahora se llama '{nuevo_nombre}'.")
    
    elif eleccion == "2": 
        try:
            nuevo_numero = int(input("Ingrese el nuevo número telefónico: "))
            contactos[nombre]["numero"] = nuevo_numero
            print(f"✅ Número actualizado para {nombre}.")
        except ValueError:
            print("❌ Debes ingresar un número válido.")
        
    elif eleccion == "3":
        nuevo_nombre = input("Ingrese el nuevo nombre: ")
        try: 
            nuevo_numero = int(input("Ingrese el nuevo numero: "))
            contactos[nuevo_nombre] = {"numero": nuevo_numero}
            del contactos[nombre]
            print(f" Contacto actualizado: {nuevo_nombre} con número {nuevo_numero}. ")
        except ValueError:
            print("❌ Número inválido. No se completó la actualización.")
    else: 
        print("❌ Opción inválida.")



# 4 - Eliminar un contacto

def eliminar_contacto():
    if contactos: 
        print("Contactos registrados: ")
        for nombre in contactos:
            print(f"- {nombre}")

        nombre = input("Ingresa el nombre del contacto que desea eliminar: ")

        if nombre in contactos:
            del contactos[nombre]
            print(f"🗑 {nombre} ha sido eliminado con exito. ")
        else: 
            print("❌ Ese contacto no esta registrado. ")
    else: 
        print("📭 No hay contactos para eliminar")

# Menu principal 

while True:
    print("\n--- Menu ---")
    print("1. Agregar contacto ")
    print("2. Mostrar contactos  ")
    print("3. Modificar contacto ")
    print("4. Eliminar contacto ")
    print("5. Salir ")

    opcion = input ("Selecciona una opcion: ")

    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        mostrar_contacto()
    elif opcion == "3":
        modificar_contacto()
    elif opcion == "4":
        eliminar_contacto()
    elif opcion == "5":
        print("Adios. ")
        break
    else:
        print("Opcion no valida, intenta de nuevo. ")
