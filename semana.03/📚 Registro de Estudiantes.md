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

# Otra version del codigo


2 #ejercicio: Registro estudiantes

# 1 - Agregar nuevo estudiante

```python

estudiantes = {}

def agregar_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ")
    if nombre in estudiantes: 
        print("Este estudiante ya esta registrado. ")
        return
    edad = int(input("Ingresa la edad del estudiante: "))
    numero = int(input("Ingresa el numero del estudiante: "))
    calificacion = float(input("Ingresa la calificacion: "))
    estudiantes[nombre] = {
        "edad": edad, 
        "numero": [numero],   # se guarda como lista 
        "calificacion": calificacion   
}
    print(f"{nombre} ha sido agregado con exito. ")

```

# 2 - Modificar la calificacion de un estudiante
    # Preguntar el nombre del estudiante.

    # Verificar si ese nombre existe en el diccionario.

    # Si existe, pedir la nueva calificación.

    # Cambiar el valor asociado a "calificacion" en el subdiccionario.
```python

def modificar_calificacion():  
    if estudiantes: 
        print("Estudiantes registrados: ")
        for nombre in estudiantes: 
            print(f"- {nombre}")

        nombre = input("Ingrese el nombre del estudiante que desea modificar: ")

        if nombre in estudiantes: 
            nueva_calificacion = float(input("Ingrese la nueva calificacion: "))
            estudiantes[nombre]["calificacion"] = nueva_calificacion
            print(f"Calificacion actualizada para {nombre}. ")
        else: 
            print("Ese estudiante no esta registrado. ")
    else: 
        print("No hay estudiantes registrados aun. ")
```

# 3 - Mostrar toda la informacion de todos los estudiantes
    #   Recorrer el diccionario estudiantes y mostrar para cada estudiante:

        #   Nombre

        #   Edad

        #   Número (aunque esté en una lista)

        #   Calificación
```python
def mostrar_estudiantes():
    if estudiantes: 
        print("\Informacion de todos los estudiantes:\n")
        for nombre, datos in estudiantes.items():
            print(f"Nombre: {nombre}")
            print(f"  Edad: {datos['edad']}")
            print(f"  Numero: {datos['numero'][0]}")    # Extraemos el primer valor de la lista y accede al primer (y único) número en la lista.
            print(f"  Calificacion: {datos['calificacion']}")
            print("-" * 30)   # Se usa un separador para que la salida sea más clara entre estudiantes.
    else:
        print("No hay estudiantes para mostrar. ")
```

# 5 - Eliminar estudiante por su nombre 
```python
def eliminar_estudiantes():
    if estudiantes:
        print("Estudiantes registrados: ")
        for nombre in estudiantes: 
            print(f"- {nombre}")

        nombre = input("Ingresa el nombre del estudiante que desea eliminar: ")

        if nombre in estudiantes: 
            del estudiantes[nombre]
            print(f"{nombre} ha sido eliminado del registro. ")
        else: 
            print("Ese estudiante no esta registrado. ")
    else: 
        print("No hay estudiantes para eliminar. ")
```

# Menu principal 
```python
while True: 
    print("\n --- Menú ---")
    print("1. Agregar estudiante. ")
    print("2. Modificar calificacion. ")
    print("3. Mostrar todos los estudiantes. ")
    print("4. Elimnar estudiantes. ")
    print("5. Salir. ")

    opcion = input("Selecciona una opcion: ")

    if opcion == '1':
        agregar_estudiante()
    elif opcion == '2':
        modificar_calificacion()
    elif opcion == '3':
        mostrar_estudiantes()
    elif opcion == '4':
        eliminar_estudiantes()
    elif opcion == '5':
        print("¡Adios!")
        break 
    else: 
        print("Opcion no valida, intenta de nuevo. ")

```



