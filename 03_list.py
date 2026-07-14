###
# 3 - Listas
# Secuescias mutables de elementos 
# Pueden contener elementos de diferentes tipos 
###

import os
os.system("clear")

# Creacion de listas 
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5]  # Lista de enteros 
lista2 = ["Manzanas", "Peras", "Platanos"] # Lista de cadenas de texto 
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos
# Ejenplo de como tambien se podria realizar  lista3: list[int | str | float | bool] = [1, "hola", 3.14, True] # lista de tipos mixtos 
lista_vacia = []
lista_de_listas = [[1, 2], [3, 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por indice
print("\nAcceso a elementos por indice")
print(lista2[0]) # Manzanas
print(lista2[1]) # Peras
print(lista2[2]) # Platanos
print(lista2[-1]) # Platanos 
print(lista2[-2]) # Peras
print(lista2[-3]) # Manzanas

print(lista_de_listas[1][0])  

# Slicing (rebanado)

lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]]
print(lista1[:3]) # [1, 2, 3]
print(lista1[3:]) # [4 ,5]
print(lista1[:]) # [1, 2, 3, 4, 5]

# HAY MAS MAGIA 
lista1 = [1, 2, 3, 4, 5, 6, 7, 8] 
print(lista1[::2]) # [1, 3, 5, 7]
print(lista1[::-1]) # Para devolver indices inversos 

# Modificar una lista 
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista 
lista1 = [1, 2, 3]

lista1 = lista1 + [4, 5, 6]
print(lista1)

# Forma mas corta y eficiente
lista1 += [7, 8, 9]
print(lista1)

###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

print("\n Ejercicio 1")
mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
print(mensaje[7:])
nuevo_mensaje = mensaje[7:10] + mensaje[10:]
print(nuevo_mensaje)


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

print("\n Ejercicio 2")
numeros = [10, 20, 30, 40, 50]
numeros[0], numeros[4] = numeros[4], numeros[0]
print(numeros)
# numeros[0] = 50 Tambien se puede pero la respuesta correcta es la anterior
# numeros[4] = 10 Tambien se puede pero la respuesta correcta es la anterior 
# print(numeros)

# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

print("\n Ejericio 3")
pan = ["pan arriba"]
ingredientes = ["jamón", "queso", "tomate"]
pan_abajo = ["pan abajo"]

sandwich = pan + ingredientes + pan_abajo
print(sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

print("\n Ejercicio 4")
lista = [1, 2, 3]
lista_nueva = lista + lista
print(lista_nueva)
# lista += [1, 2, 3] tambien se puede pero la forma correcta es la anterior 
# print(lista) tambien se puede pero la forma es la anterior 

# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

print("\n Ejercicio 5")
lista = [10, 20, 30, 40, 50]
print(lista[2:3])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]
print("\n Ejercici 6")
lista = [1, 2, 3, 4, 5, 6]
# print(lista[3:])
# print(lista[2::-1])
lista_nueva = lista[2::-1] + lista[3:]
print(lista_nueva)