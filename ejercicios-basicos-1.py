# Solicita al usuario que ingrese una palabra o frase
texto = input("Escribe algo: ")

# Crea una lista que contiene el texto repetido 5 veces
# Ejemplo: si texto = "Hola" → ["Hola", "Hola", "Hola", "Hola", "Hola"]
# Luego, utiliza el método join para unir todos los elementos de la lista
# con un guion "-" como separador, resultando en: "Hola-Hola-Hola-Hola-Hola"
dato = "-".join([texto] * 5)

# Muestra el resultado final en pantalla
print(dato)
