# Calculadora de operaciones básicas
# Crea una función calculadora(a, b, operacion) que reciba dos números y la operación (suma, resta, multiplicacion, division) y retorne el resultado.

import math


def calculadora(a, b, operacion):
    """
    Calcula la operación básica entre dos números.

    Parámetros:
    a (float): Primer número
    b (float): Segundo número
    operacion (str): 'suma', 'resta', 'multiplicacion' o 'division'

    Retorna:
    float: Resultado de la operación
    """
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        if b != 0:
            return a / b
        else:
            return "Error: División entre 0"
    else:
        return "Operación no válida"


numero1 = float(input("Por favor selecciona el primer número: "))
numero2 = float(input("Por favor selecciona el segundo número: "))
operacion = input(
    "Por favor selecciona la operación (suma, resta, multiplicacion, division): ")

print("El resultado es: ", calculadora(numero1, numero2, operacion))


# Conversor de unidades
# Haz una función convertir_km_millas(km) que convierta kilómetros a millas (1 km = 0.621371 millas).

def conversor_k(kilometros):

    mill = kilometros * 0.621371
    return mill


def conversor_m(millas):

    km = millas / 0.621371
    return km


operacion = input("Selecciona que quieres convertir kilometros / millas :")
cantidad = float(input("selecciona las unudades que deseas convertir: "))

if operacion == "kilometros":
    millas = conversor_k(cantidad)
    print(f"{cantidad} km = {millas} millas")

else:
    kilometros = conversor_m(cantidad)
    print(f"{cantidad} millas = {kilometros} km")

# Sin variables intermedias


def conversor_kilometros(kilometros):
    return kilometros * 0.621371  # devolvemos directo


def conversor_millas(millas):
    return millas / 0.621371      # devolvemos directo


operacion = input(
    "Selecciona que quieres convertir kilometros / millas: ").strip().lower()
cantidad = float(input("Selecciona las unidades que deseas convertir: "))

if operacion == "kilometros":
    print(f"{cantidad} km = {conversor_kilometros(cantidad)} millas")
else:
    print(f"{cantidad} millas = {conversor_millas(cantidad)} km")

# Versión mejorada del conversor (con repetición)


def conversor_kilom(kilometros):
    return kilometros * 0.621371


def conversor_mill(millas):
    return millas / 0.621371


while True:
    print("\n=== CONVERSOR DE UNIDADES ===")
    operacion = input(
        "Selecciona qué quieres convertir (kilometros/millas) o 'salir' para terminar: ").lower()

    if operacion == "salir":
        print("Gracias por usar el conversor. ¡Hasta luego!")
        break  # rompe el bucle y termina el programa

    cantidad = float(input("Selecciona las unidades que deseas convertir: "))

    if operacion == "kilometros":
        print(f"{cantidad} km = {conversor_kilom(cantidad)} millas")
    elif operacion == "millas":
        print(f"{cantidad} millas = {conversor_mill(cantidad)} km")
    else:
        print("Opción no válida, intenta de nuevo.")


# Promedio de una lista
# Crea una función promedio(lista) que reciba una lista de números y devuelva el promedio.

def promedio(lista):
    return sum(lista) / len(lista)


print("\n=== Calculadora de promedio ===")
print("Ingresa los números que deseas promediar o escribe 'salir' para terminar.\n")

numeros = []

while True:
    entrada = input("Número: ")

    if entrada.lower() == "salir":
        break

# con manejo de errores y excepciones

    try:
        numero = float(entrada)  # convierte el input a número
        numeros.append(numero)
    except ValueError:
        print("⚠️ Entrada no válida, ingresa un número o 'salir'.")

# Mostrar promedio solo si hay números
if numeros:
    print(f"\nEl promedio de {numeros} es: {promedio(numeros)}")
else:
    print("No ingresaste ningún número.")


# Factorial con función
# Escribe factorial(n) que calcule el factorial de un número usando un bucle.

def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


print(factorial(5))

# Usando while


def factorial1(n):
    resultado = 1
    while n > 1:
        resultado *= n
        n -= 1
    return resultado


print(factorial1(5))


# Usando un bucle y range descendente
def factorial2(n):
    resultado = 1
    for i in range(n, 0, -1):
        resultado *= i
    return resultado


print(factorial2(5))


# Función con *args
# Escribe multiplicar_todos(*numeros) que multiplique todos los números pasados como argumentos.

def multiplicar_todos(*numeros):
    resultado = 1
    for n in numeros:
        resultado *= n
    return resultado


print(multiplicar_todos(2, 4, 2, 1, 3))


# En una sola línea con math.prod


def multiplicar_todos1(*numeros):
    return math.prod(numeros)


print(multiplicar_todos1(2, 4, 2, 1, 3))

# Documentar tu función favorita
# Escoge cualquiera de las funciones anteriores y agrega una docstring bien escrita.


def multiplicar_todos2(*numeros):
    """
    Multiplica todos los números pasados como argumentos.

    Parámetros:
        *numeros (int o float): Una cantidad variable de números a multiplicar.

    Retorna:
        int o float: El producto de todos los números dados.

    Ejemplo:
        >>> multiplicar_todos(2, 4, 2, 1, 3)
        48
    """
    resultado = 1
    for n in numeros:
        resultado *= n
    return resultado


print(multiplicar_todos2(2, 4, 2, 1, 3))
