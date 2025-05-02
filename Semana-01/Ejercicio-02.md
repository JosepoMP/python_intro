# Ejercicio 02 📚

```python
# ejercicio 2 
edad = int(input("¿Cuantos años tienes?"))
pase = input("¿Tienes pase dorado?:")

if edad < 18:
    print ("no puedes ingresar al club")
elif pase == "si" and edad > 18: 
    print ("puedes entrar al club")
elif pase == "no" and (edad > 18 and edad < 25):
    print ("puedes entrar al club")
elif pase == "no" and edad > 25:
    print ("estas muy viejo, no puedes ingresar al club")
```
