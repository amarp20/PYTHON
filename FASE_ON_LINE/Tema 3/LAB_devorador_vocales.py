vocales = "aeiouAEIOU"
palabra = input("Ingrese una palabra: ")

for letra in palabra:
    if letra in vocales:
        continue
    print(letra)
