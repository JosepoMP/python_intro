# sistema validacion de productos
```python
# CONVERTIR ENTRADA A NÚMEROS

def convertir_a_numero(entrada):

    # 1. Elimina los puntos en los números
    entrada = entrada.replace(".", "")

    # 2. Intenta convertir el número a entero directamente
    try:
        return int(entrada)
    finally: print  ("")

# DATOS DE ENTRADA

# Producto
print("Ingresa el nombre del producto:")
producto = input()

# Obtener precio
precio = None
while precio is None or precio <= 0:
    entrada_precio = input("Ingresa el precio por unidad: ")
    precio = convertir_a_numero(entrada_precio)
    if precio is None or precio <= 0:
        print("El precio debe ser un número positivo.")

# Obtener cantidad
cantidad = None
while cantidad is None or cantidad <= 0:
    entrada_cantidad = input("Ingresa la cantidad de productos que llevas: ")
    cantidad = convertir_a_numero(entrada_cantidad)
    if cantidad is None or cantidad <= 0:
        print("La cantidad debe ser un número positivo.")



# PROCESAMIENTO

# Cálculo de subtotal
subTotal = precio * cantidad

# Obtener descuento
print("Ingresa el descuento (presiona Enter si NO aplica):")
entrada_descuento = input()

if entrada_descuento.strip() == "":
    desc = 0.0
else:
    entrada_descuento = entrada_descuento.replace("%", "")
    try:
        desc = float(entrada_descuento)
        if not 0 <= desc <= 100:
            print("El descuento debe estar entre 0% y 100%. Se aplicará 0%.")
            desc = 0.0
    except ValueError:
        print("Descuento inválido. Se aplicará 0%.")
        desc = 0.0

# Calcular total
total = subTotal - (subTotal * desc / 100)


# DATOS DE SALIDA

print(f"\nResumen de compra:")
print(f"\nProducto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio por unidad: ${precio:,.2f}")
print(f"Subtotal: ${subTotal:,.2f}")
print(f"Descuento aplicado: {desc}%")
print(f"\nTOTAL A PAGAR: ${total:,.2f}")
```
