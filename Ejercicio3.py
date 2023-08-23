def contar_palabras(cadena):

    palabras = cadena.split()

    frecuencia = {}
    
    for palabra in palabras:
        # Eliminar signos de puntuación y convertir a minúsculas para evitar duplicaciones
        palabra = palabra.strip(".,!?").lower()
        
        # Si la palabra ya está en el diccionario, incrementa su frecuencia
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            # Si no está en el diccionario, agrégala con una frecuencia inicial de 1
            frecuencia[palabra] = 1

    return frecuencia


cadena = input("Ingrese una cadena de caracteres: ")

resultado = contar_palabras(cadena)

print("Frecuencia de palabras:")
for palabra, frecuencia in resultado.items():
    print(f"{palabra}: {frecuencia}")
