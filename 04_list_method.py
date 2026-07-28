###
#  04 - lista de metodos
# los metodos mas  importantes para trabajar con listas 
###
## TRUCO PARA LIMPIAR LA CONSOLA 

import os
os.system("clear")

lista1 = ['a', 'b', 'c', 'd']

# añadir o insertar elementos a la lista 

lista1.append('e') # añade un elemento al final 
print(lista1)

lista1.insert(1, '@') # insertar un elemento en la posicion que le indiquemos como primer argumento 
print(lista1)

lista1.extend(['🎶', '👀']) # agregar elementos al final de la lista 
print(lista1)

# Eliminar elementos de la lista 
lista1.remove('@')
print(lista1) # Eliminar la aparicion de la primera cadena de texto (@)

ultimo = lista1.pop() # Eliminar el ultimo de la lista 
print(ultimo)
print(lista1)

lista1.pop(1)  # Eliminar el segundo elemtno de la lista (es el indice 1)
print(lista1)

# Eliminar por lo bestia
del lista1[-1]
print(lista1)

lista1.clear() # Eliminar todos los elementos de la lista 
print(lista1)

# DELET (del) Para eliminar un rango de elementos 
lista1 = ['😂', '💁🏽', '😴', '🙈']
del lista1[3:]
print(lista1)

# Mas metodos utiles

print('ordenar listas modificando la original')
numbers = [3, 12, 43, 8, 34, 65, 4]
numbers.sort()
print(numbers)

print('Ordenando listas creando una nueva lista')
numbers = [3, 12, 43, 8, 34, 65, 4]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

print("Ordenar una lista de cadenas de texto") # Todo minuscula 
frutas = ['manzana', 'pera', 'limon', 'mango', 'mora', 'fresa', 'arandanos']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto") # Mezcla entre mayuscula y minuscula 
frutas = ['Manzana', 'pera', 'Limon', 'Mango', 'mora', 'Fresa', 'arandanos']
frutas.sort(key=str.lower)
print(frutas)
# key: parámetro que indica con qué criterio se ordenarán los elementos.
# = : asigna ese criterio al parámetro key.
# str.lower: convierte temporalmente cada texto a minúsculas para compararlo,
# permitiendo ordenar correctamente aunque haya mayúsculas y minúsculas.

##### PARA QUE SE USA (), [], {}

# ()  Paréntesis
# - Llamar funciones: print(), len(), sorted()
# - Pasar argumentos a una función.
# - Agrupar operaciones matemáticas.
# - Crear tuplas: (1, 2, 3)

# []  Corchetes
# - Crear listas: [1, 2, 3]
# - Acceder a elementos por índice: lista[0]
# - Modificar elementos: lista[1] = 10
# - Hacer slicing: lista[1:4]

# {}  Llaves
# - Crear diccionarios: {"nombre": "Oscar", "edad": 25}
# - Crear conjuntos (set): {1, 2, 3}
# - Un diccionario vacío se crea con {}.
# - Un conjunto vacío se crea con set().

# Mas cosas utiles 
animals = ['🐶', '🐱', '🐭', '🐶']
print(len(animals)) # Tama;o de la lista -->  4
print(animals.count('🐶')) # Cuantaas veces aparece el '🐶' --> 2
print('🐼' in animals) # Comprueba si hay un 🐼 en la lista 
print('🐭' in animals) # Comprueba si hay un 🐭 en la lista 


####### EJERCICIOS ########

# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

print("\nEjercicio 1")
lista2 = [1, 2, 3, 4, 5]
lista2.append(6)
print(lista2)

lista2.insert(2, 10)
print(lista2)

lista2[0] = 0
print(lista2)


# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().


print("\n Ejercicio 2")
lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]

lista_a.extend(lista_b)
print(lista_a)

lista_a.remove(1)
print(lista_a)

numero_faltante = lista_a.pop(3)
print(numero_faltante)

lista_b.clear()
print(lista_b)


# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

print("\n Ejercicio 3")

lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del lista3[2:5]
print(lista3)


# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

print("\n Ejercicio 4")

lista4 = [5, 2, 8, 1, 9, 4, 2]

lista4.sort()
print(lista4)

print(lista4.count(2))

print(7 in lista4)


# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

print("\n Ejercicio 5")
original = [1, 2, 3]
copia_1 = original[0:]

copia_2 = original.copy()

referencia = original

original[0] = 10


print(copia_1)
print(copia_2)
print(referencia)
print(original)


# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

print("\n Ejercicio 6")

fruits = ["Manzana", "pera", "BANANA", "naranja"]
fruits.sort(key=str.lower)
print(fruits)
