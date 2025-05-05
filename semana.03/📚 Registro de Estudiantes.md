# jercicio: Registro de Estudiantes

# Objetivo: 
# Crear un diccionario para almacenar información sobre estudiantes y realizar algunas operaciones básicas como agregar, modificar y mostrar datos.       

#instrucciones:

    #1. Crea un diccionario llamado estudiantes, donde las claves sean los nombres de los estudiantes y los valores sean otro diccionario con las claves edad y calificacion.

    #2. El programa debe permitir al usuario realizar las siguientes operaciones:
        #Agregar un nuevo estudiante (nombre, edad, calificación).
        #Modificar la calificación de un estudiante.
        #Mostrar la información de todos los estudiantes.
        #Eliminar un estudiante por su nombre.
```python

def agregar_estudiante(Estudiantes):
    nombre = input("Introduce el nombre del estudiante: ")
    edad = int(input("Introduce la edad del estudiante: "))
    calificacion = float(input("Introduce La calificacion del estudiante: "))

    # Agregar el estudiante al diccionario 

    Estudiantes[nombre] = {'edad': edad, 'calificacion': calificacion}
    print(f"Estudiante {nombre} agregado exitosamente.")

def modificar_calificacion(Estudiantes):
    nombre = input("Introduce el nombre del estudiante cuya calificacion desea modificar: ")

    # Verificar si el estudiante existe 

    if nombre in Estudiantes:
        nueva_calificacion = float(input(f"Introduce la nueva calificacion para {nombre}: "))
        Estudiantes[nombre]['calificacion'] = nueva_calificacion
        print(f"la calificacion de {nombre} ha sido actualizada a {nueva_calificacion}. ")

    else:
        print("Estudiante no se encuentra en el registro.")

def mostrar_estudiantes(Estudiantes):
    if Estudiantes: 
        print("Lista de estudiantes: ")
        for nombre, info in Estudiantes.items():
            print(f"nombre: {nombre}, edad: {info['edad']}, calificacion: {info['calificacion']}")
    else:
        print("No hay estudiantes registrados. ")

def eliminar_estudiante(Estudiantes):
    nombre = input("Introduce el nombre del estudiante que desea eliminar: ")

    # Verificar si el estudiante existe en el diccionario 

    if nombre in Estudiantes:
        del Estudiantes[nombre]  # Eliminar al estudiante 
        print(f"estudiante {nombre} ha sido eliminado. ")
    else: 
        print("El estudiante no se encuentra en el registro. ")

# Funcion principal que muestra el menu 
def main(): 
    Estudiantes={}

    while True:
        print("\nOpciones: ")
        print("1. Agregar Estudiante.")
        print("2. Modificar Calificacion.")
        print("3. Mostrar Estudiantes.")
        print("4. Eliminar Estudiantes.")
        print("5. Salir.")

        opcion = input("Elige una opcion (1-5): ")

        if opcion == '1':
            agregar_estudiante(Estudiantes)
        elif opcion == '2':
            modificar_calificacion(Estudiantes)
        elif opcion == '3':
            mostrar_estudiantes(Estudiantes)
        elif opcion == '4':
            eliminar_estudiante(Estudiantes)
        elif opcion == '5':
            print("¡Adios!")
            break
        else: 
            print("Opcion no valida, intenta de nuevo. ")

# ejecutar el programa 
if __name__== "__main__":
    main()
```
