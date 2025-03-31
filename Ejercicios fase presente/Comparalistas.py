lista1 = [1,2,3,4,5,6]
lista2 = [1,2,3,4,5,6]
lista3 = ["a","b",3,4,5,6]
lista4 = ["a","b",3,4,5,6,7]

def compara_lon(a,b):
    if len(a) == len(b):
        return True
    else:
        return False

def compara_ind(a,b, counter=0):
    if compara_lon(a,b):
        for i in range(len(a),):
            if a[i] == b[i]:
                continue
            elif a[i] != b[i]:
                counter+=1
                continue
        return(f"La longitud de las listad es la misma, y tienen {counter} elementos diferentes")
    else:
        return(f"Las longitudes de de las lista no son iguales, la primera lista tiene {len(a)} elementos y la segunda lista tiene {len(b)} elementos.")

print(compara_ind(lista1, lista3))
