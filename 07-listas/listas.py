# Ejercicio: Práctica básica con listas en Python

# Paso 1: Crear una lista de al menos 5 elementos.
# Escribe aquí tu lista con al menos 5 elementos.
lista1= [1,2,3,4,5]

# Paso 2: Mostrar el primer y el último elemento usando índices.
# Usa índices para acceder al primer y último elemento de la lista e imprímelos.
print(lista1[0])
print(lista1[-1])

# Paso 3: Agregar un nuevo elemento a la lista.
# Usa el método append() para agregar un nuevo elemento a la lista.
lista1.append(6)
print(lista1)

# Paso 4: Eliminar un elemento por su valor.
# Usa el método remove() para eliminar un elemento específico de la lista.
lista1.remove(6)
print(lista1)

# Paso 5: Imprimir cuántos elementos tiene la lista.
# Usa la función len() para contar los elementos de la lista e imprímelo.
print(len(lista1))