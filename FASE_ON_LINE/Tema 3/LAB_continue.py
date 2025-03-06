
vocales = 'AEIOU'
sinVocales = ''
palabra = input('Ingrese una palabra: ')
palabra = palabra.upper()
 
for letra in palabra:
    if letra not in vocales:
        sinVocales = sinVocales + letra
    else:
        continue
 
print(letra + sinVocales, sep='\n')