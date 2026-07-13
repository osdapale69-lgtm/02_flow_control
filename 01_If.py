##
# sentencias condicionales (if, elif, else)
# if: si la condición es verdadera, ejecuta el bloque de código)
# elif: si la condición anterior es falsa, y esta condición es verdadera, ejecuta el bloque de código)
# else: si todas las condiciones anteriores son falsas, ejecuta el bloque de código)
# permiten ejecutar bloques de código dependiendo de si una condición es verdadera o falsa.
## 
import os
os.system("clear")

print("\n Sentencia simple condicional if")

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")

edad = 16
if edad >= 18:
    print("Eres mayor de edad")
    print("¡Felicidades!")
 
     
print("\n Sentencia simple condicional else")
edad = 15 
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("\n Sentencias condicionales elif")
nota = 7
if nota >= 9:
    print("!SOBRESALIENTE!")
elif nota >= 7:
    print("!NOTABLE!")
elif nota >= 5:
    print("!APROBADO!")
else:
    print("!NO ESTA CALIFICADO!")


print("\n Condicionales multiples")
edad = 15
tiene_carnet = False

if edad >= 18 and tiene_carnet:
    print("Puedes conducir")
else: 
    print("No puedes conducir")

if edad >= 18 or tiene_carnet:
    print("Puedes conducir en isla margarita")
else:
    print("Paga al policia y conduce en isla margarita")

es_fin_de_semana = False
if not es_fin_de_semana:
    print("midu, venga a trabajar")

print("\n anidar condicionales")
edad = 20 
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes salir de fiesta")
    else:
        print("No puedes salir de fiesta, no tienes dinero")
else:
    print("No puedes salir de fiesta, eres menor de edad")


# Mas facil:
# if edad < 18:
#     print("No puedes salir de fiesta, eres menor de edad")
# elif tiene_dinero:
#     print("Puedes salir de fiesta")
# else:
#     print("No puedes salir de fiesta, no tienes dinero")    

numero = 5
if numero: #True si numero es diferente de cero
    print("El numero no es cero")

numero = 0
if numero: #False si numero es cero
    print("Aca no entrara nunca")

nombre = ""
if nombre:
    print("el nombre no es vacio ")


numero = 3 #Asignacion 
es_el_tres = numero == 3 #Comparacion

if es_el_tres:
    print("el numero es 3")


print("\nLa condicion ternaria:")
# es una forma concisa de hacer un if-else en una linea de codigo
# [codigo si cumple la condicion] if [condicion] else [codigo si no cumple]

edad = 17 
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)


