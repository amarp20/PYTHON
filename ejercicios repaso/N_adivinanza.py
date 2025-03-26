'''Ejercicio 14: Juego de adivinanza
Crea una clase Adivinanza que genere un número aleatorio entre 1 y 100 (usa random).
Incluye un método que permita al usuario adivinar y devuelva pistas ("más alto" o "más bajo") hasta que acierte.'''

import random

class Adivinanza:

    def __init__(self, numero=0):
        self.numero = numero

    def generar_numero(self):
        self.numero = random.randint(1,100)

    def juego(self):
        counter = 0
        while True:
            try:
                eleccion = int(input("Elige un número entero entre el 1 y el 100: "))
                if eleccion > self.numero and eleccion >=0 and eleccion <=100:
                    print(f"{eleccion} es más alto que el numero que escogí.")
                    counter +=1
                elif eleccion < self.numero and eleccion >=0 and eleccion <=100:
                    print(f"{eleccion} es más bajo que el numero que escogí.")
                    counter +=1
                elif eleccion == self.numero:
                    print(f"¡¡¡GANASTE EN TAN SOLO {counter} INTENTOS!!!")
                    break
                else:
                    print("Te he dicho que entre 0 100, que no te enteras!!!!.")
                    counter +=1
            except Exception as e:
                print(f"Que paza killo, que es ezo que has escribio?")
                


adivinar = Adivinanza()
adivinar.generar_numero()
adivinar.juego()