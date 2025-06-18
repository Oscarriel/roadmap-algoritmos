# Archivo: condicionales.py
# Este archivo está diseñado para que practiques estructuras condicionales en Python.

# ¿Qué es un condicional?
# Un condicional es una estructura que permite ejecutar un bloque de código solo si se cumple una condición.
# En Python, usamos las palabras clave `if`, `elif` y `else` para crear condicionales.

# Ejemplo básico:
# if condicion:
#     # Código que se ejecuta si la condición es verdadera
# elif otra_condicion:
#     # Código que se ejecuta si la primera condición es falsa y esta es verdadera
# else:
#     # Código que se ejecuta si ninguna de las condiciones anteriores es verdadera

# Cómo pedir un número al usuario:
# Puedes usar la función `input()` para obtener datos del usuario. Recuerda que `input()` devuelve una cadena,
# así que debes convertirla a un número usando `int()` o `float()` si es necesario.

# Ejemplo:
# numero = int(input("Ingresa un número: "))

# Instrucciones:
# 1. Pide al usuario que ingrese un número.
# 2. Determina si el número es positivo, negativo o cero.
#    - Usa un condicional `if`, `elif`, `else` para verificar cada caso.
# 3. Determina si el número es par o impar.
#    - Usa el operador `%` (módulo) para verificar si el número es divisible entre 2.

# Estructura inicial del código:

# Paso 1: Pedir al usuario que ingrese un número
numero = int(input("Ingresa un número: "))
if numero > 0:
    print(f"El numero {numero}, es mayor")
elif numero > 0:
    print(f"El numero {numero}, es menor")
else:
    print("El numero es 0")

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
# ¡Ahora completa el código siguiendo las instrucciones y experimenta con diferentes números!

