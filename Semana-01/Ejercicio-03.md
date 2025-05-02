# Ejercicio "Mi pareja ideal" 📚  

```python
# Ejercico 03

puntaje = 0
pregunta1 = input("¿eres aseado? ")
if pregunta1 == "si":
    puntaje = puntaje + 50
    pregunta2 = input("¿te lavas el cabello por lo menos 2 dias? ")
    if pregunta2 == "si":
        puntaje = puntaje + 50
    elif pregunta2 == "talvez":
        puntaje = puntaje + 20
    else: puntaje = puntaje - 10

else:
    pregunta1 = input("¿pero se baña? ")
    if pregunta1 == "si":
        puntaje = puntaje + 5

pregunta3 = input ("¿mides mas de 1,80? ")
if pregunta3 == "si":
    puntaje = puntaje + 80

else: 
    pregunta3 = input("¿Al menos mayor a 1,75? ")
    if pregunta3 == "si":
        puntaje = puntaje + 10

pregunta4 = input("¿Estudias o tienes planes de? ")
if pregunta4 == "si": 
    puntaje = puntaje + 1
    pregunta5 = input("¿Que estudias o que quieres estudias? ")
    if pregunta5 == "programacion":
        puntaje = puntaje + 80
    else: puntaje = puntaje - 100
        
pregunta6 = input("¿Tienes mas de 20 años? ")
if pregunta6 == "si":
    puntaje = puntaje + 20
elif pregunta6 == "no":
    puntaje = puntaje - 100000000

pregunta7 = input("¿Vas al gym o haces algun deporte?... ")
if pregunta7 == "si": 
    puntaje = puntaje + 90
elif pregunta7 == "no":
    puntaje = puntaje - 100 

pregunta8 = input("¿te gustan los animales?")
if pregunta8 == "si":
    puntaje = puntaje + 50 
elif pregunta8 == "no":
    puntaje = puntaje - 50

if puntaje >= 100:
    print("Perfectisimo!")
elif puntaje > 50:
    print("Ni si Ni no")
else: 
    print("Gas con Fo")
#calcular total de puntos
total = puntaje 
print(f"Su total de puntos es: {total:}")
```
