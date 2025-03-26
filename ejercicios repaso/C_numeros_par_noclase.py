'''Ejercicio 3: Lista de números pares
Crea una clase Numeros con un atributo que sea una lista de enteros.
Incluye un método que devuelva solo los números pares de esa lista.'''

class pares:
    
    def __init__(self, lista):
        self.lista = lista
    
    def set_numero(self, numero):
        self.numero = numero
    
    def contar_pares(self):
        for i in self.lista:
            if i % 2 == 0:
                print(i)
    
    def meter_numeros(self):
        while True:
            self.numero = int(input("Introduzca un número para añadirlo a la lista.\nPara dejar de introducir números y extraer los pares introduzca 0: "))
            if self.numero != 0:
                self.lista.append(self.numero)
            else:
                par.contar_pares()
                break
lista = []
par = pares(lista)
par.meter_numeros()