numbers=[10, 5, 7, 2, 1]
print("contenido de la lista:  ", numbers)
numbers[0]=111
print("nuevo contenido de la lista:  ", numbers) #hemos cambiado el valor del primer elemento de la lista.

numbers[1]=numbers[4]
print("nuevo contenido de la lista:  ", numbers) #hemos cambiado el valor del segundo elemento por el del quinto elemento de la lista.

print(numbers[0]) #muestra el valor de ese elemento

print("\nLongitud de la lista:   ", len(numbers))

del(numbers[1])
print("\nLongitud de la lista:   ", len(numbers)) #hemos eliminado un numero de la lista y pedimos la nueva longitud.

print(numbers[-1])

numbers.append(7) #Otra forma de anadir un valor a la lista es con el metodo .append()
print(numbers)

print(numbers[0] + numbers[1]) #manera de sumar el valor en primera y segunda posicion

numbers.insert(1, 15) #Ccon este metodo anadimos el valor en la posicion deseada
print(numbers)

my_list=[]
for i in range(5):
    my_list.append(i+1) #anade 1 a la lista en cada salto del bucle sumando 1 cada vez
print(my_list)

my_list=[]
for i in range(5):
    my_list.insert(0, i+1) #anade 1 al principio de la lista en cada salto del bucle sumando 1 cada vez
print(my_list)

my_list=[10, 1, 8, 3, 5]
total=0
for i in range(len(my_list)):#El rango sera la longitud de my_list
    total += my_list[i]#en cada salto suma el siguiente valor de my_list
print(total)#muestra la suma de los valores de la lista

my_list=[10, 1, 8, 3, 5]
total=0
for i in my_list:#El rango sera my_list
    total += i#en cada salto suma el siguiente valor de my_list
print(total)#muestra la suma de los valores de la lista

my_list[0], my_list[4] = my_list[4], my_list[0] #al hacer esto intercambiamos los valores segun sus posiciones
my_list[1], my_list[3] = my_list[3], my_list[1] #el resultado dara la vuelta al orden de los valores
print(my_list)

my_list=[1, 2, 3, 4, 5, 6, 7, 8, 9 ,10]
for i in range(len(my_list) // 2):
    my_list[i], my_list[len(my_list) -i -1] = my_list[len(my_list) -i -1], my_list[i]
print(my_list)


