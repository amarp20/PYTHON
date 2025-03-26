'''Ejercicio 10: Simulador de dado
Escribe una clase Dado que simule tirar un dado de 6 caras (usando random).
Incluye un método para tirar el dado y otro para mostrar el resultado.
EXTRA: Añade un selector de tipos de dados (d2, d4, d6, d8, d10, d12, d20)'''

import random

class Dado:
    
    d2 = [1,2]
    d4 = [1,2,3,4]
    d6 = [1,2,3,4,5,6]
    d8 = [1,2,3,4,5,6,7,8]
    d10 = [1,2,3,4,5,6,7,8,9,10]
    d12 = [1,2,3,4,5,6,7,8,9,10,11,12]
    d20 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    def __init__(self):
        pass
    
    def selector(self):
        
        while True:
            try: 
                tipo=int(input("Elija el número de caras de su dado (2,4,6,8,10,12,20), o pulse 1 para salir: "))
                if tipo == 2:
                    print(random.choice(self.d2))
                elif tipo == 4:
                    print(random.choice(self.d4))
                elif tipo == 6:
                    print(random.choice(self.d6))
                elif tipo == 8:
                    print(random.choice(self.d8))
                elif tipo == 10:
                    print(random.choice(self.d10))
                elif tipo == 12:
                    print(random.choice(self.d12))
                elif tipo == 20:
                    print(random.choice(self.d20))
                elif tipo == 1:
                    print("gracias por lanzar el dado")
                    break
                else:
                    print("El número de caras introducido no está disponible.")
                    
                
            except Exception:
                print("El valor introducido no es válido.")
                self.selector()
            
    
tirada = Dado()
tirada.selector()
    