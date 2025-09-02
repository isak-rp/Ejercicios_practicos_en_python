# Ejemplo con break
for numero in range(10):
    if numero == 5:
        break
    print(numero)

# Ejemplo con continue
for numero in range(10):
    if numero % 2 == 0:
        continue
    print(numero)   # Solo imprime impares

# continue salta el resto del código dentro del bucle y va directo a la siguiente vuelta.
# Sin continue, el bucle sigue ejecutando todo el bloque.

# 💡 Piensa en continue como un "saltar esta vuelta".
# Y en break como "salir del bucle de inmediato".


# ✅ Ejercicio 1:
# Imprime los números del 1 al 20 con un bucle for.

for numero in range(1, 21):
    print(numero)

# ✅ Ejercicio 2:
# Imprime los números pares del 1 al 50 usando while.
numero = 0

while numero <= 50:
    numero += 1
    if numero % 2 == 0:
        print(numero)

# Funciona, pero vamos a hacerlo más ordenado:

# Inicias en 0, pero incrementas antes de imprimir.

# Esto imprime bien los pares hasta 50, pero incrementas primero, lo que puede confundir al leer.

# Se puede optimizar evitando el if si incrementas de 2 en 2.

# 🔹 Versión más limpia:

numero = 2

while numero <= 50:
    print(numero)
    numero += 2
# Más eficiente: ya no revisa todos los números, solo los pares.


# ✅ Ejercicio 3:
# Haz una cuenta regresiva desde 10 hasta 1 y al final imprime "¡Despegue!".
despegue = 10
while despegue >= 0:
    print(despegue)
    despegue -= 1
    if despegue == 0:
        print("¡Despegue!")
        break

# version sin el break

despegue = 10
while despegue > 0:
    print(despegue)
    despegue -= 1
    if despegue == 0:
        print("¡Despegue!")


# version sin usar un if
despegue = 10
while despegue > 0:
    print(despegue)
    despegue -= 1

print("¡Despegue!")


# ✅ Ejercicio 4:
# Pide un número al usuario y muestra su tabla de multiplicar del 1 al 10.

numero = int(input("Ingresa el número a multiplicar"))
tabla = 1
while tabla <= 10:
    print(f"{numero * tabla}")
    tabla += 1


#  Versión mejorada:
numero = int(input("Ingresa el número a multiplicar: "))
tabla = 1

while tabla <= 10:
    print(f"{numero} x {tabla} = {numero * tabla}")
    tabla += 1
# 📌 Ahora el programa imprime la operación completa, así será más entendible.

# ✅ Ejercicio 5:
# Pide palabras al usuario hasta que escriba "salir".
# Luego imprime todas las palabras que escribió.

    # palabras = []

    # while palabras != "salir":
    #     palabras.append(
    #         input.lower("""Escribe cualquier palabra si escribes "salir" se acaba."""))


# ✅ Versión corregida:

palabras = []  # Lista vacía para guardar las palabras

while True:
    palabra = input(
        'Escribe cualquier palabra (escribe "salir" para terminar): ').lower()

    if palabra == "salir":
        break  # Salimos del bucle si el usuario escribe "salir"

    palabras.append(palabra)  # Guardamos la palabra en la lista

# Imprimimos todas las palabras que escribió el usuario
print("Palabras ingresadas:", palabras)


# 💡 Explicación:
# while True: → Creamos un bucle infinito controlado por break.

# palabra = input(...).lower() → Guardamos la palabra en minúsculas para que "Salir", "SALIR" o "salir" se reconozcan igual.

# if palabra == "salir": break → Salimos del bucle si el usuario escribe "salir".

# palabras.append(palabra) → Guardamos la palabra en la lista.

# Al final, imprimimos la lista completa.


# ✅ Ejercicio 6 (extra creativo):
# Haz un programa que dibuje un triángulo de asteriscos según un número que ingrese el usuario.

# Pedimos al tamaño del triángulo
filas = int(input("Ingrese el número de filas para el triángulo: "))

# Bucle para dibujar cada fila
for i in range(1, filas + 1):
    print("*" * i)
