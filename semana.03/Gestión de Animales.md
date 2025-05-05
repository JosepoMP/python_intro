# 🐾 Ejercicio: Gestión de Animales
# Desarrolla un programa en Python que permita gestionar información sobre animales. El programa debe tener un menú usando funciones con las siguientes opciones: ** recuerda que pasa nombre, edad y enfermo cada uno debe de guardarse en su propia lista

# 1. Agregar un animal:
#El usuario debe ingresar el nombre, la edad y si el animal está enfermo o no (sí/no). Esta información debe ser almacenada en tres listas separadas: una para los nombres de los animales, otra para sus edades y otra para su estado de salud.

#2. Eliminar un animal por su nombre:
#El usuario debe poder ingresar el nombre del animal que desea eliminar. Si el animal está registrado, debe ser removido de las tres listas. Si el animal no está registrado, se debe mostrar un mensaje indicando que no se encontró.

#3. Listar todos los animales registrados:
#El programa debe mostrar una lista con todos los animales registrados, incluyendo su nombre, edad y estado de salud (enfermo/sano).

#4. Salir:
#El programa debe permitir al usuario salir del menú.

# ----------------------------------------------------------------------------------

```python

# Agregar animal 

def agregar_animal(nombres, edades, salud):
    nombre = input("Introduce el nombre del animal: ")
    edad = int(input("Introduce la edad del animal: "))
    estado_salud = input("¿El animal esta enfermo? (si/no): ").strip().lower()

    nombres.append(nombre)
    edades.append(edad)
    salud.append(estado_salud)

    print(f"{nombre} ha sido agregado al registro")

# Eliminar animal

def eliminar_animal(nombres, edades, salud):
    nombre = input("Introduzca el nombre del animal que desea eliminar: ")

    if nombre in nombres: 
        indice = nombres.index(nombre)
        # eliminar en las tres lineas usando el mismo indice 
        nombres.pop(indice)
        edades.pop(indice)
        salud.pop(indice)
        print(f"{nombre} ha sido eliminado del registro. ")
    else: 
        print("El animal no esta registrado. ")

# Listar animales 

def listar_animales(nombres, edades, salud):
    if nombres:     # verificamos si hay animales registrados
        print("\nAnimales registrados: ")
        for i in range(len(nombres)): 
            print(f"Nombre: {nombres[i]}, Edad: {edades[i]}, Enfermo: {salud[i]}")
    else:
        print("No hay animales registrados")


def menu():
    nombres = []
    edades = []
    salud = []

    while True:
        print("\n--- Menú de Gestrion de Animales ---")
        print("1. Agregar un animal: ")
        print("2. Eliminar un animal por su nombre: ")
        print("3. Listar todos los animales registrados: ")
        print("4. salir")

        opcion = input("Eligue una opcion (1-4): ")

        if opcion == "1":
            agregar_animal(nombres, edades, salud)
        elif opcion == "2":
            eliminar_animal(nombres, edades, salud)
        elif opcion == "3":
            listar_animales(nombres, edades, salud)
        elif opcion == "4":
            print("¡Adios!")
            break
        else: 
            print("Opcion no valida, intenta de nuevo.")

# ejecutar el programa 
if __name__ == "__main__":
    menu()
```
