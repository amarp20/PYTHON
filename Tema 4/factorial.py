def factorial_iterativo(n):
    resultado=1
    for i in range (2, n+1):
        resultado*=i
    print(resultado)

factorial_iterativo(9)
