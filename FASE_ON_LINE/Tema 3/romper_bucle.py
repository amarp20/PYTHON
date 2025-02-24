largest_number=-9999999999999
number=int(input("Introduce un numero o escribe -1 para detener:   "))
while number != -1:
    if number>largest_number:
        largest_number=number
    number=int(input("Introduce un numero o escribe -1 para detener:   "))
print("El numero mas grande es:   ", largest_number)
