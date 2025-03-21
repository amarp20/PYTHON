'''Ejercicio 6: Ordenar una lista
Escribe una función que reciba una lista de números y la ordene de menor a mayor sin usar sort().
Luego, intégrala como método en una clase Ordenador.'''

class Ordenador():
    
    lista=[1,35,16,103,94,109,3,7]
    
    def __init__(self):
        pass
        
    def ordenar(self):    
        for _ in range(len(self.lista)):
            for i in range(len(self.lista)-1):
                if  self.lista[i] > self.lista[i+1]:
                    self.lista[i], self.lista[i+1] = self.lista[i+1], self.lista[i]
                else:
                    continue
        return self.lista
    
ordenar = Ordenador()
print(ordenar.ordenar())
        
