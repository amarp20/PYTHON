lista1 = [1,2,3,4,5,6]
lista2 = [1,2,3,4,5,6]
lista3 = [1,2,3,4,5,6]
lista4 = ["a","b","3","4","5","6","7"]
lista5 = ["a","b","3","4","5","6","7"]

lista_a=[]

while True:
    num=str(input("introduce un carácter diferente a 0 para añadirlo a la lista:  "))
    if num!=str(0):
        lista_a.append(num)
    else:
        break

def compara_lon(a,b,c):
    if len(a) == len(b) and len(b) == len(c):
        return True
    else:
        return False

def compara_ind(a,b,c, counter=0):
    if compara_lon(a,b,c):
        for i in range(len(a)):
            if a[i] == b[i] and b[i] == c[i]:
                continue
            else:
                return("aunque la longitud de las listas es la misma no tienen los mismos elementos")
        return("La longitud de las listad es la misma y tienen los mismos elementos")
            
    else:
        return(f"Las longitudes de de las lista no son iguales, la primera lista tiene {len(a)} elementos, la segunda lista tiene {len(b)} elementos, la tercera lista tiene {len(c)} elementos.")

print(compara_ind(lista4, lista5, lista_a))