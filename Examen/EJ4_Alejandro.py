'''Realiza una aplicación a tu elección que tenga una función útil.
La aplicación debe utilizar como minimo:
función o funciones
al menos un bucle for y un bucle while
al menos un if, un else y un elif
el código debe estar comentado correctamente en donde sea necesario.'''

import random

class Jugar_estudiar():

    jugadas = ["blanca", "negra"] #en esta lista guardamos los valores que utilizaremos en caso de querer jugar al juego de las piedras

    def __init__(self):
        pass

    def set_persona(self, persona):
        self.persona = persona

    def elegir_jugada(self):
        while True: #Si en el menú inicial se elige jugar vendrá aquí inicialmente, luego a jugada, en este caso elegimos salir al menú inicial después de cada jugada, a no ser se elija un valor no válido
                jugador=input("Elige 1 para blanca ó 2 para negra: ")
                if jugador == "1":
                    self.persona = "blanca"
                    break
                elif jugador == "2":
                    self.persona = "negra"
                    break
                else:
                    print("Hemos dicho 1 ó 2.")

    def jugada(self):
        maquina = random.choice(self.jugadas) #con esta función la máquina elige uno de los dos valores aleatoriamente y luego valoramos cada una de las posibilidades
        if self.persona == "blanca" and maquina == "blanca":
            print(f"Has ganado, yo tenía una piedra {maquina}.")
        elif self.persona == "negra" and maquina == "negra":
            print(f"Has ganado, yo tenía una piedra {maquina}.")
        elif self.persona == "negra" and maquina == "blanca":
            print(f"Has perdido, yo tenía una piedra {maquina}.")
        elif self.persona == "blanca" and maquina == "negra":
            print(f"Has perdido, yo tenía una piedra {maquina}.")
            
    def tabla(self):#Si en el menú inicial se elige estudiar vendrá aquí
        
        num=int(input("Introduzca un número:   "))  
        for i in range (1,11):
            print(f"{num}x{i}={num*i}") #con este bucle iteramos en un rango de 1 a 10 multiplicando i en cada iteración por el número, al ser un for simple al hacer cada tabla volverá al menú inicial
        
    def a_jugar(self): #Una vez creada la partida como clase Jugar_estudiar se mete en este menú que le da a elegir entre jugar o estudiar
        while True:
            seguir = input(f"Elige una opción:\n1. Para jugar al juego de las piedras.\n2. Para estudiar mates haciendo tablas.\nCualquier otra cosa para terminar\n")
            if seguir == "1": #Al elegir que los valores sean string nos aseguramos de que cualquier valor será válido para su gestión
                self.elegir_jugada()
                self.jugada()
            elif seguir == "2":
                self.tabla()
            else:
                print("Gracias por elegirnos, ya sea para jugar o estudiar.")
                break #La única manera de salir del bucle inicial es presionando una tecla diferente a 1 ó 2

partida = Jugar_estudiar()
partida.a_jugar()