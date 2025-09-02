# ✅ Ejercicio 1:
# Crea una lista con 5 frutas y muestra cada una en mayúsculas usando un bucle.

frutas = ["manzana", "pera", "platano", "uva", "kiwi"]

for fruta in frutas:
    print(fruta.upper())

# 📌 Tip: Si quisieras guardarlas en mayúsculas en otra lista, podrías usar listas por comprensión:

frutas_mayus = [fruta.upper() for fruta in frutas]
print(frutas_mayus)


# ✅ Ejercicio 2:
# Crea una tupla con 3 números y calcula su suma y promedio.

numeros = (4, 7, 3)
suma = sum(numeros)

print(
    f"""Esta es la suma de la tupla: {suma} \nEste es el promedio de la tupla: {suma / len(numeros):.2f}""")


# ✅ Ejercicio 3:
# Crea un diccionario con la información de una persona: nombre, edad y ciudad.
# Luego imprime: "Isaac tiene 24 años y vive en México".

persona = {
    "nombre": "Isaac",
    "edad": 24,
    "ciudad": "México"
}

print(
    f"{persona['nombre']} tiene {persona['edad']} años y vive en {persona['ciudad']} ")


# 📌Utilizando una funcion para despues agregar más personas

# Diccionario inicial
persona = {
    "nombre": "Isaac",
    "edad": 24,
    "ciudad": "México",
    "profesion": "Estudiante"
}


# Función que recibe un diccionario y devuelve un mensaje


def presentar_persona(p):
    # Usamos .get() para evitar errores si falta alguna clave
    nombre = p.get("nombre", "Desconocido")
    edad = p.get("edad", "Desconocida")
    ciudad = p.get("ciudad", "Desconocida")
    profesion = p.get("profesion", "")

    return f"{nombre} tiene {edad} años, vive en {ciudad} y trabaja/estudia como {profesion}."


# Llamamos a la función
mensaje = presentar_persona(persona)
print(mensaje)

persona2 = {
    "nombre": "",
    "edad": 0,
    "ciudad": "",
    "profesion": ""
}

persona2["nombre"] = input("ingresa el nombre de la persona: ").capitalize()
persona2["edad"] = int(input("ingresa la edad de la persona: "))
persona2["ciudad"] = input("ingresa la ciudad de la persona: ").capitalize()
persona2["profesion"] = input(
    "ingresa la profesion de la persona: ").capitalize()

mensaje = presentar_persona(persona2)
print(mensaje)


# ✅ Ejercicio 4:
# Pide 5 números al usuario y guárdalos en un set.
# Imprime el set y asegúrate que no haya números repetidos.
numeros = set()  # Creamos un conjunto vacío

for i in range(5):  # Pedimos 5 números
    nuevo_numero = int(input(f"Ingresa el número {i+1} (0 al 10): "))
    numeros.add(nuevo_numero)  # Se añaden al conjunto

print(f"Los números sin repetir son: {numeros}")


# 📌 con un set comprhension

numero = {int(input(f"ingresa el número {i+1} (0 al 10): ")) for i in range(5)}
print(f"Estos son los números sin repetir: {numero}")


# ✅ Ejercicio 5 (extra creativo):
# Crea una lista de palabras, elimina las repetidas usando un set y vuelve a convertirlo en lista.
# Luego imprime la lista ordenada alfabéticamente.

palabras = ["uno", "dos", "tres", "cuatro", "dos", "uno", "dos"]
palabras_sin_repetir = set(palabras)
print(palabras)

print(palabras_sin_repetir)

palabras = sorted(palabras_sin_repetir)
print(palabras)

# 📌 con comprhension

words = sorted(set(["uno", "dos", "tres", "cuatro", "dos", "uno", "dos"]))
print(f"estas son las palabras ordenadas sin repatir: {words}")


# 🚀 Ejercicios extra para subir dificultad:

# ✅Listas por comprensión con frutas: Crea una lista con las frutas que tengan más de 4 letras.

frutas = ["manzana", "plátano", "pera", "manzana",
          "uva", "fresa", "plátano", "kiwi", "uva"]

nueva_lista = [x for x in frutas if len(x) > 4]
print(f"Esta la lista de frutas mayor a cuatro letras: {nueva_lista}")

# ✅Dada una tupla de números, encuentra el mayor y el menor usando max() y min().

numeros = (1, 2, 7, 3, 7, 8, 44, 36, 75, 3, 6, 2, 87, 1)
maximo = max(numeros)
minimo = min(numeros)
print(f"el maximo es: {maximo} y el minimo es: {minimo}")
