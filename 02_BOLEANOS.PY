##
# 02 - booleanos
# valores logicos: true (verdadero) y false (falso)
# fundamental para el control de flujo y la logica de los programas
##
# los booleanos representan  valores de verdad: true (verdadero) y false (falso)

import os
os.system("clear")

print("\nValores booleanos basicos")
print(True)
print(False)

# Operadores de  comparacion: devuelven un valor booleano (true o false)
print("\nOperadores de comparacion")
print("5 > 3:", 5 > 3) # true
print("5 < 3:", 5 < 3) # false
print("5 == 5:", 5 == 5) # true (igualdad)
print("5 != 3:", 5 != 3) # true (desigualdad) 
print("5 >= 5:", 5 >= 5) # true (mayor o igual)
print("5 <= 3:", 5 <= 3) # false (menor o igual)

print("\n Comparacion de cadenas de texto")
print("Manzana < Pera:", "Manzana" < "Pera") # true
print("'Hola' == 'hola':", "Hola" == "hola") # False

# Operadores logicos: and, or, not
print("\nOperadores logicos")
print("True and True:", True and True) # true
print("True and False:", True and False) # false
print("True or False:", True or False) # true
print("False or False:", False or False) # false
print("not True:", not True) # false      
print("not False:", not False) # true

# Tabla de verdad (para referencias)
print("\n Tabla de verdad")

print("\n and:")
print("A     B     A and B")
print("True  True  ", True and True)
print("True  False ", True and False)
print("False True  ", False and True)
print("False False ", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True  ", True or True)
print("True  False ", True or False)
print("False True  ", False or True)
print("False False ", False or False)

print("\n not:")
print("A     not A")
print("True  ", not True)
print("False ", not False)
