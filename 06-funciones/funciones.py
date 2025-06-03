    # Guía para practicar funciones en Python

    # 1. Definir una función:
    #    Se utiliza la palabra clave `def` seguida del nombre de la función y paréntesis.
    #    Dentro de los paréntesis se pueden definir parámetros si la función los necesita.
    #    El cuerpo de la función debe estar indentado.
    #    Recuerda reemplazar `pass` con el código necesario para cada función.

    # Función 1: saludo()
    # In
  #    tabla(7) strucciones:
    # - Definir una función llamada `saludo` que no reciba parámetros.
    # - Dentro de la función, mostrar un mensaje de saludo utilizando `print`.

def saludo():
    print("Hola!")

    # Función 2: suma(a, b)
    # Instrucciones:
    # - Definir una función llamada `suma` que reciba dos parámetros: `a` y `b`.
    # - La función debe retornar la suma de `a` y `b`.

def suma(a, b):
    print(a + b)
    

    # Función 3: es_par(n)
    # Instrucciones:
    # - Definir una función llamada `es_par` que reciba un parámetro `n`.
    # - La función debe retornar `True` si `n` es un número par, y `False` si es impar.

def es_par(n):
    if n == 0:
        print("0 es un numero par")
    elif n % 2 == 0:
        return True
    else:
        return False

    # Función 4: tabla(n)
    # Instrucciones:
    # - Definir una función llamada `tabla` que reciba un parámetro `n`.
    # - La función debe retornar una cadena con la tabla de multiplicar del número `n` del 1 al 10.
    # - Cada línea de la tabla debe estar separada por un salto de línea (`\n`).

def tabla(n):
    resultado = ""
    for i in range(1,11):
        linea = f"{n} * {i} = {n * i}\n"
        resultado += linea
    return resultado 

    # Nota:
    # - Probar llamando a cada función desde el bloque principal del programa.
    # - Utilizar `if __name__ == "__main__":` para ejecutar las pruebas.
    # - Ejemplo: Llamar a `saludo()`, `suma(3, 5)`, `es_par(4)`, y `tabla(7)` para verificar su funcionamiento.

if __name__ == "__main__":
    saludo()
    suma(3, 5)
    print(es_par(4))
    print(tabla(7))