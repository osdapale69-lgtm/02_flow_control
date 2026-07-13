###
# EJERCICIOS
###

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

# mi codigo

# numero = input("Escribe dos números separados por un espacio").split()
# primer_numero = int(numero[0])
# segundo_numero = int(numero[1])

# if primer_numero > segundo_numero:
#     print(f"El numero mayor es {primer_numero}")
# elif primer_numero < segundo_numero:
#     print(f"El numero mayor es {segundo_numero}")
# elif primer_numero == segundo_numero:
#     print("SON NUMEROS IGUALES")

# codigo profesor youtube 

# print("\nEjercicio 1:")
# num1 = int(input("Introduce el primer número: "))
# num2 = int(input("Introduce el segundo número: "))

# if num1 > num2:
#     print(f"{num1} es mayor que {num2}")
# elif num2 > num1:
#     print(f"{num2} es mayor que {num1}")
# else:
#     print("Los números son iguales")


# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

# print("\n Ejercicio2")
# num_1 = int(input("introduce el primer numero: "))
# num_2 = int(input("introduce el segundo numero: "))
# operacion = input("introduce una operacion (+, -, *, /)")

# if operacion == "+":
#     print(num_1 + num_2)
# elif operacion == "-":
#     print(num_1 - num_2)
# elif operacion == "*":
#     print(num_1 * num_2)
# elif operacion == "/":
#     if num_2 == 0:
#         print("NO SE PUEDE REALIZAR OPERACION")
#     else:
#         print(num_1 / num_2)
# else:
#     print("Operacion no valida")



# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

print("\n Ejercicio 3")
año = int(input("A continuacion dijitar año para determinar si es bisiesto "))

if  año % 400 == 0:
    print(f"el año digitado es {año} por lo cual quiere decir que si es bisiesto")
elif año % 100 == 0:
    print(f"el año digitado es {año} por lo cual quiere decir que no es bisiesto")
elif año % 4 == 0:
    print(f"el año digitado es {año} por lo cual quiere decir que si es bisiesto")
else:
    print(f"el año digitado es {año} por lo cual quiere decir que no es bisiesto")

# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)
# - Adulto mayor (65 años o más)

# print("\n Ejercicio 4")
# edad = int(input("A continuacion introduzca su edad para clasificarlo.\n"))

# if edad <= 2:
#     print("pertenece a categoria de Bebe")
# elif edad <= 12:
#     print("pertenece a categoria de Niño")
# elif edad <= 17:
#     print("pertenece a categoria de Adolescente")
# elif edad <= 64:
#     print("pertenece a categoria de Adulto")
# else:
#     print("pertenece a categoria de Adulto mayor")
