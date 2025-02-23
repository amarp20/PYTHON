# coding: latin1
# Escribir una función que muestre por pantalla la tabla de multiplicar (del 1 al 10).
# La función se llamará "tabla" y no recibirá ningún parámetro ni hace uso del return.
# SOLO ESTA PERMITIDO UTILIZAR LA FUNCIÓN PRINT() UNA ÚNICA VEZ DENTRO DE LA FUNCIÓN
# Desarrolle el código necesario dentro de la función para que esa instrucción print() imprima la tabla de multiplicar del 1 al 10 con el formato:
# Ejemplo:
# 1 x 1 = 1
# 1 x 2 = 2
# Debe hacer una llamada a la función para que se ejecute.

def tabla(n):
    z=1
    for i in range(n):
        b=z
        a=1
        c=a*b
        print(a, "x", b, "=", c)
        b+=1
        z=b
       

tabla(10)

# hecho por mi:

def tabla1():
   
    for i in range(11):
        print(1,"x",i,"=",i)

tabla1()

# y la tabla del 2

def tabla2():
    v=0
    for i in range(11):
        print(2,"x",i,"=",v)
        v+=2

tabla2()
