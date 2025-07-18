# operadores.py
# Este archivo es una guía para practicar operadores en Python.

# ¿Qué son los operadores?
# Los operadores son símbolos que le indican al intérprete de Python que realice una operación específica.
# Por ejemplo, pueden ser usados para realizar cálculos matemáticos, comparar valores, entre otros.

# Instrucciones:
# 1. Solicita dos números al usuario utilizando la función input() y conviértelos a tipo entero o flotante según sea necesario.
# 2. Realiza las operaciones indicadas en cada sección y utiliza print() para mostrar los resultados.

# Solicitar dos números al usuario
# num1 = ...
# num2 = ...

# Operaciones matemáticas básicas
# Realiza las siguientes operaciones con los números ingresados:
# - Suma (+)
# - Resta (-)
# - Multiplicación (*)
# - División (/)
# - Módulo (%)
# - Potencia (**)
# - División entera (//)
# Ejemplo:
# resultado_suma = num1 + num2
# print("La suma es:", resultado_suma)

# Operaciones comparativas
# Realiza las siguientes comparaciones entre los números ingresados:
# - Igualdad (==)
# - Diferente (!=)
# - Menor que (<)
# - Mayor que (>)
# - Menor o igual que (<=)
# - Mayor o igual que (>=)
# Ejemplo:
# es_igual = num1 == num2
# print("¿Son iguales?", es_igual)

# Espacio para que el estudiante complete las operaciones y muestre los resultados.
notas = []
cantidad = int(input("¿Cuantas notas deseas ingresar? :"))
for i in range(cantidad):
    nota= float(input(f"Inserta la nota numero {i+1}: "))
    notas.append(nota)
print("Notas del curso: ", end="")
for nota in notas:
    print(f"{nota} ", end=", ")
promedio= sum(notas)/len(notas)
print()
print(f"El promedio del curso es de {promedio}")
if promedio >= 4:
    print(f"El estudiante aprobo el curso con promedio {promedio}")
else:
    print(f"El promedio de curso {promedio}, no es suficiente para aprobar el curso")

