# bucles.py
# Archivo guía para aprender sobre bucles en Python.

# 1. Escribe un bucle `for` que imprima los números del 1 al 10.
# Pista: Usa la función range().
for i in range(0, 11):
    print(i)
# 2. Escribe un bucle `for` que recorra una lista de nombres y los salude.
# Pista: Crea una lista de nombres y usa un bucle para iterar sobre ella.
nombres = ["Juan", "Joan", "Yonkeiberson"]
for i in nombres:
    print(f"¡Hola! {i}")
# 3. Escribe un bucle `while` que continúe pidiendo texto al usuario 
# hasta que escriba "salir".
# Pista: Usa input() para obtener texto del usuario y una condición para detener el bucle.
texto = ""
while texto.lower().strip() != "salir":
    texto = input("Dame texto :")

# 4. Escribe una función que reciba un número como parámetro y use un bucle `for` 
# para imprimir la tabla de multiplicar de ese número.
# Pista: Define una función con def y usa range() dentro del bucle.
def tabla(n):
    for i in range (1, 11):
        print(n * i)
tabla(9)