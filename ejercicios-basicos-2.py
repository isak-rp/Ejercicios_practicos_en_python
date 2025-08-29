# ✅ejercicio 1
# pide dos números al usuario y muestra las operaciones

numero1 = input("Ingresa el primer número: ")
numero2 = input("Ingresa el segundo número: ")

while True:
    if numero1 != int or float:
        print("Ingresa un número valido ")

    if numero2 != int or float:
        print("Ingresa un número valido ")

    break

print(f"La suma es: {numero1} + {numero2}")
print(f"La resta es: {numero1} - {numero2}")
print(f"El producto es: {numero1} * {numero2}")
print(f"El cociente es: {numero1} / {numero2}")
print(f"El resto de la division es: {numero1} % {numero2}")


# ✅Ejercicio 1 corregido

# Pedimos los números y los convertimos a float para permitir decimales
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Mostramos los resultados
print(f"La suma es: {numero1 + numero2}")
print(f"La resta es: {numero1 - numero2}")
print(f"El producto es: {numero1 * numero2}")
print(f"El cociente es: {numero1 / numero2}")
print(f"El resto de la división es: {numero1 % numero2}")


# -----------------------------------------------------------------------------------------
# ✅Ejercicio 2:
# Pide al usuario su edad y muestra:
# Si es mayor o menor de edad
# Si tiene exactamente 18 años, muéstrale "Acabas de alcanzar la mayoría de edad"

edad = int(input("Porfavor ingresa tu edad: "))

if edad == 18:
    print("Acabas de alcanzar la mayoría de edad.")

elif edad > 18:
    print("Eres mayor de edad.")

elif edad < 18:
    print("Eres menor de edad.")


# -------------------------------------------------------------------------------------
# ✅mini-reto.

# Haz un programa que pida tres números y muestre:
# La suma de los tres.
# El número mayor.
# El número menor.
# Usa solo comparaciones (if/else), sin max() ni min() todavía.

numero1 = int(input("Ingresa el primer número"))
numero2 = int(input("Ingresa el segundo número"))
numero3 = int(input("Ingresa el tercer número"))

print(f"La suma de los tres números es: {numero1 + numero2 + numero3}")

if numero1 > numero2 and numero3:
    print(f"El número mayor es: {numero1}")
elif numero2 > numero1 and numero3:
    print(f"El número mayor es: {numero2}")
elif numero3 > numero2 and numero1:
    print(f"El número mayor es: {numero3}")

else:
    print("No hay un número mayor")

if numero1 < numero2 and numero3:
    print(f"El número menor es: {numero1}")
elif numero2 < numero1 and numero3:
    print(f"El número menor es: {numero2}")
elif numero3 < numero2 and numero1:
    print(f"El número menor es: {numero3}")

else:
    print("No hay un número menor")


# Corrección para mayor claridad
# La condición correcta es comparar cada número con los otros dos:

numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))
numero3 = int(input("Ingresa el tercer número: "))

print(f"La suma de los tres números es: {numero1 + numero2 + numero3}")

# Determinar el mayor
if numero1 > numero2 and numero1 > numero3:
    print(f"El número mayor es: {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El número mayor es: {numero2}")
elif numero3 > numero1 and numero3 > numero2:
    print(f"El número mayor es: {numero3}")
else:
    print("No hay un número mayor (puede que sean iguales)")

# Determinar el menor
if numero1 < numero2 and numero1 < numero3:
    print(f"El número menor es: {numero1}")
elif numero2 < numero1 and numero2 < numero3:
    print(f"El número menor es: {numero2}")
elif numero3 < numero1 and numero3 < numero2:
    print(f"El número menor es: {numero3}")
else:
    print("No hay un número menor (puede que sean iguales)")
# 💡 Explicación de la corrección
# numero1 > numero2 and numero1 > numero3 → asegura que numero1 sea mayor que los dos.

# Igual para numero2 y numero3.

# Si no se cumple ninguno, entramos al else, lo que significa que al menos dos son iguales.


# -------------------------------------------------------------------------------------------------
# ✅Ejercicio 3:
# Pide al usuario un número y verifica:
# Si es par o impar
# Si es múltiplo de 5

    # numero_del_usuario = int(input("Ingresa tu número: "))

    # for verificar in numero_del_usuario:
    #     verificar /= 2
    # if  verificar == 0:
    #     print("Tu número es par.")
    # else:
    #     print("Tu número es impar.")

# Problemas en el código:
# for verificar in numero_del_usuario:
# numero_del_usuario es un número entero, y no se puede recorrer con un for (eso se hace con listas, strings, etc.).
# Aquí no necesitas un for, solo una división con el operador módulo %.
# verificar /= 2 ❌
# Eso divide entre 2, pero no sirve para saber si es par o impar.
# Lo que se usa es el módulo (%), que devuelve el residuo de una división.

# Código corregido ✅

numero_del_usuario = int(input("Ingresa tu número: "))

# Verificar si es par o impar
if numero_del_usuario % 2 == 0:
    print("Tu número es par.")
else:
    print("Tu número es impar.")

# Verificar si es múltiplo de 5
if numero_del_usuario % 5 == 0:
    print("Tu número es múltiplo de 5.")
else:
    print("Tu número NO es múltiplo de 5.")

# Explicación paso a paso:

# numero_del_usuario % 2 == 0 → si al dividir entre 2 el residuo es 0, el número es par.
# numero_del_usuario % 5 == 0 → si al dividir entre 5 el residuo es 0, el número es múltiplo de 5.


# -----------------------------------------------------------------------------
# ✅ Ejercicio 4:
# Un restaurante da 10% de descuento si la cuenta es mayor a $100.
# Pide el total al usuario y muestra cuánto debe pagar con el descuento (si aplica).
cuenta = float(input(
    "Hay un 10% de descuento si tu cuenta es mayor a $100. \n Total de la cuenta: "))

if cuenta > 100:
    descuento = cuenta * .10
    # Para mostrar solo dos dígitos después del punto decimal en Python, puedes usar la función round() o el formato de cadena con el especificador .2f. La función round() redondea el número al número especificado de decimales, mientras que el formato de cadena permite controlar la presentación visual sin modificar el valor subyacente.
    print(f"Total con descuento es : ${cuenta - descuento:.2f}")

else:
    print(f"El descuento no es aplicable. \n Total: ${cuenta}")
# Una forma más moderna de formatear cadenas en Python es usando f-strings.

# numero = 3.14159
# cadena_formateada = f"{numero:.2f}"
# print(cadena_formateada)  # Salida: 3.14


# Solo un par de detalles que te pueden interesar para mejorarlo aún más:

# Redondeo también cuando no aplica el descuento
# En tu else, estás mostrando el total sin formatear (${cuenta}), lo que puede mostrar muchos decimales (por ejemplo 100.3333333). Sería mejor mostrarlo también con :.2f.

# Evitar repetir lógica
# En lugar de imprimir en cada rama (if y else), puedes calcular el monto final en una variable y luego imprimirlo una sola vez. Eso lo hace más limpio.

# 👉 Aquí una versión optimizada:

cuenta = float(input(
    "Hay un 10% de descuento si tu cuenta es mayor a $100. \nTotal de la cuenta: "))

if cuenta > 100:
    cuenta -= cuenta * 0.10  # Aplica el descuento

print(f"Total a pagar: ${cuenta:.2f}")
# Con esto:

# Si la cuenta es 120, paga 108.00.

# Si la cuenta es 80, paga 80.00.


# -------------------------------------------------------------------------------------------------------------
# ✅Ejercicio 5 (extra creativo):
# Pide al usuario 3 números y muéstralos ordenados de mayor a menor
# (puedes usar operadores lógicos y comparaciones, sin funciones de listas todavía 😉).

primer_numero = int(input("Selecciona tu primer número"))
segundo_numero = int(input("Selecciona tu segundo número"))
tercer_numero = int(input("Selecciona tu tercer número"))

if primer_numero >= segundo_numero and primer_numero >= tercer_numero:
    if segundo_numero >= tercer_numero:
        print(primer_numero, segundo_numero, tercer_numero)
    elif tercer_numero >= segundo_numero:
        print(primer_numero, tercer_numero, segundo_numero)

if segundo_numero >= primer_numero and segundo_numero >= tercer_numero:
    if primer_numero >= tercer_numero:
        print(segundo_numero, primer_numero, tercer_numero)
    elif tercer_numero >= primer_numero:
        print(segundo_numero, tercer_numero, primer_numero)

if tercer_numero >= segundo_numero and tercer_numero >= primer_numero:
    if segundo_numero >= primer_numero:
        print(tercer_numero, segundo_numero, primer_numero)
    elif primer_numero >= segundo_numero:
        print(tercer_numero, primer_numero, segundo_numero)


# Con listas el ejercicio se vuelve muchísimo más corto y elegante, porque Python ya tiene métodos para ordenar.
# Mira la diferencia:

# ✅Ejercicio con listas
numeros = []  # creamos una lista vacía

# Pedimos los 3 números y los guardamos en la lista
numeros.append(int(input("Selecciona tu primer número: ")))
numeros.append(int(input("Selecciona tu segundo número: ")))
numeros.append(int(input("Selecciona tu tercer número: ")))

# Ordenamos la lista de mayor a menor
numeros.sort(reverse=True)

# Mostramos el resultado
print("Números ordenados de mayor a menor:", numeros)

# 🔎 Explicación rápida:
# append() → mete cada número en la lista.
# sort(reverse=True) → ordena la lista, y con reverse=True lo hace de mayor a menor.
# Si no pones reverse=True, lo hace de menor a mayor.


# 👉 aún más compacto:

numeros = [
    int(input("Selecciona tu primer número: ")),
    int(input("Selecciona tu segundo número: ")),
    int(input("Selecciona tu tercer número: "))
]

print("De mayor a menor:", sorted(numeros, reverse=True))
