#code:latin1
def tabla(num):
    
    for i in range (1,11):
        print(str(num) + "x" + str(i) + "=" + str(num*i))
        print(f"{num}x{i}={num*i}")
        print(" ")
        
numero=int(input("Introduzca un número:   "))       
tabla(numero)
print(f"El número que has utilizado es: {numero}")