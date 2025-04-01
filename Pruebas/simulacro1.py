'''Realice un programa que reciba como parámetros 2 números enteros.
La función sumará todos los números entre esos dos números, ambos incluidos.
Finalmente imprimirá en pantalla el número obtenido.'''

def sumar_rango(a,b):
    lista = []
    lista.append(a)
    lista.append(b)
    
    if lista[0]>lista[1]:
        lista[0], lista[1] = lista[1], lista[0]

    w=lista[1]
    v=lista[0]
    while True:
        if v < w-1:
            v+=1
            lista.append(v)
        else:
            return sum(lista)
        
print(sumar_rango(9,1))