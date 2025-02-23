for i in range(10):
    print("El valor de i es:   ",i)

print(" ")

for i in range(3):
    print(i, end=" ")

print(" ")

valores = {'j': 1, 'a': 3, 'm': 7, 'e': 9, 's': 40}
for x in valores:
  print("clave", x, end=" | ") # accede a la clave
  print("valor:", valores[x]) # accede a los valores

for y in valores.values(): # accede a los valores
  print(y)

for z in valores.keys(): # accede a la clave
  print(z)

w = valores.items() # dicta los caracteres
print(type(w), w)

for a, b in w: 
  print("clave:", a, " | valor: ", b)

print(" ")

for v in range(2):
    print("El valor de v es:   ", v) # muestra los valores del rango 0 a 1
for a in range(2, 8):
    print("El valor de a es:   ", a) # muestra los valores del rango 2 a 7
for i in range(2, 8, 3):
    print("El valor de i es:   ", i) # muestra los valores del rango 2 a 7 en intervalos de 3

print(" ")

for i in range(6,1,-2):
    print(i, end=" ")

