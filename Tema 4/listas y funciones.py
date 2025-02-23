def list_sum(lst):
    s=0

    for i in lst:
        s+=i

    return s

print(list_sum([5,4,3,7,9,14]))

#------------------------------------------

def suma_extrana(n):
    suma_estrana=[]

    for i in range(0, n):
        suma_estrana.insert(0, i)
    return suma_estrana

print(suma_extrana(5))

