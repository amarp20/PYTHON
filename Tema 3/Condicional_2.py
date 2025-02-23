number1=int(input("Ingresa el primer numero:   "))
number2=int(input("Ingresa el segundo numero:   "))
number3=int(input("Ingresa el tercer numero:   "))
largest_number=number1
if number2>largest_number:
    largest_number=number2
if number3>largest_number:
    largest_number=number3
print("El numero mas grande es:   ",largest_number)