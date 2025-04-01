def sumar_rango(a,b):
    lista = []
    lista.append(a)
    lista.append(b)
    
    if lista[0]>lista[1]:
        lista[0], lista[1] = lista[1], lista[0]

    b=lista[1]
    a=lista[0]
    for i in range(a+1, b):
        lista.append(i)    
    return sum(lista)
        
print(sumar_rango(9,1))