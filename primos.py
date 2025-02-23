'''
def es_primo(num):
    if num<2:
        return False
    else:
        for i in range(2,(num-1)):
            if num % i == 0:
                return False
        return True
        
def lista_primos():
    primos=[]
    for i in range(2,101):
        if es_primo(i):
            primos.append(i)
    return primos

print(lista_primos())
'''
def es_primo():
    primos=[]
    for i in range(2,101):
        for j in range(2,i-1):
            if i % j == 0:
                break
        else:
            primos.append(i)
    print(primos)
    
es_primo()
    
