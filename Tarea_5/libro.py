frecuencia_palabras={}

try:
    with open('Clases/crimen.txt', 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            palabras=linea.lower().replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('-', '').replace('_', '').replace('(', '').replace(')', '').replace(';', '').replace(':', '').split()
            
            for palabra in palabras:
                if palabra in frecuencia_palabras:
                    frecuencia_palabras[palabra] += 1
                else:
                    frecuencia_palabras[palabra] = 1

except FileNotFoundError:
    print("El archivo 'crimen.txt' no se encuentra en el directorio.")

palabras_ordenadas=sorted(frecuencia_palabras.items(), key=lambda x: x[1], reverse=True)

palabras_unicas = set(frecuencia_palabras.keys())

print("Las 10 palabras más frecuentes son:")
for palabra, frecuencia in palabras_ordenadas[:10]:
    print(f"{palabra}: {frecuencia}")

print(f"\nNúmero total de palabras únicas: {len(palabras_unicas)}")

print("\nPalabras que se repiten más de 3 veces:")
for palabra, frecuencia in palabras_ordenadas:
    if frecuencia > 3:
        print(f"{palabra} : {frecuencia}")