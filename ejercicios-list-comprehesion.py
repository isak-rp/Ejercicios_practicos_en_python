# Una Comprehension List es una forma concisa de crear listas en Python, pues permite generar listas nuevas transformando cada elemento de una colección existente o creando elementos a partir de un rango. La sintaxis es compacta y directa, lo que facilita la comprensión del propósito de tu código de un vistazo.

# La estructura básica de una Comprehension List es:

# [expresión for elemento in iterable if condición]
# Que se traduce a: “Crea una nueva lista evaluando nueva_expresión para cada elemento en el iterable.”

# Ejercicios:

# Doble de los Números
# Dada una lista de números [1, 2, 3, 4, 5], crea una nueva lista que contenga el doble de cada número usando una List Comprehension.

lista = [1, 2, 3, 4, 5]
nueva_lista = [x*2 for x in lista]
print(f"lista con valores duplicados: {nueva_lista}")

# Filtrar y Transformar en un Solo Paso
# Tienes una lista de palabras ["sol", "mar", "montaña", "rio", "estrella"] y quieres obtener una nueva lista con las palabras que tengan más de 3 letras y estén en mayúsculas.

palabras = ["sol", "mar", "montaña", "rio", "estrella"]
p = [x.upper() for x in palabras if len(x) > 3]
print(f"Estas son las palabras en mayusculas con mas de tres letras: {p} ")

# Crear un Diccionario con List Comprehension
# Tienes dos listas, una de claves ["nombre", "edad", "ocupación"] y otra de valores ["Juan", 30, "Ingeniero"]. Crea un diccionario combinando ambas listas usando una List Comprehension.

llaves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]
persona = {llaves[i]: valores[i] for i in range(len(llaves))}
print(f"Esta es la descripcion de la persona: {persona}")

# Anidación de List Comprehensions
# Dada una lista de listas (una matriz):
# matriz = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# Calcula la matriz traspuesta utilizando una List Comprehension anidada.

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

filas = len(matriz)
columnas = len(matriz[0])

m = [[matriz[i][j] for i in range(filas)] for j in range(columnas)]
print(f"Esta es la matriz transpuesta: {m}")

# Con zip + list comprehension (más corto)

transpuesta_zip = [list(fila) for fila in zip(*matriz)]

print("Transpuesta (con zip):")
print(transpuesta_zip)

# Extraer Información de una Lista de Diccionarios
# Dada una lista de diccionarios que representan personas:
# personas = [
#     {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
#     {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
#     {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
#     {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
# ]
# Extrae una lista de nombres de personas que viven en “Madrid” y tienen más de 30 años.

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

personas_filtradas = [p["nombre"]
                      for p in personas if p["ciudad"] == "Madrid" and p["edad"] > 30]

print(f"Estas son las personas de Madrid mayores de 30: {personas_filtradas}")

# List Comprehension con un else
# Dada una lista de números [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], crea una nueva lista multiplicando por 2 los números pares y dejando los impares como están.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista2 = [x * 2 if x % 2 == 0 else x for x in lista]

print(lista2)
