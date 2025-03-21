import random

class Juego():

    jugadas = ["piedra", "papel", "tijera"]

    def __init__(self):
        pass

    def set_persona(self, persona):
        self.persona = persona

    def elegir_jugada(self):
        while True:
                jugador=input("Elige 1 para piedra 2 papel y 3 para tijera: ")
                if jugador == "1":
                    self.persona = "piedra"
                    break
                elif jugador == "2":
                    self.persona = "papel"
                    break
                elif jugador == "3":
                    self.persona = "tijera"
                    break
                else:
                    print("Que hace killo 1, 2 ó 3")

    def jugada(self):
        maquina = random.choice(self.jugadas)
        if self.persona == "papel" and maquina == "papel":
            print(f"El humano sacó {self.persona} la máquina sacó {maquina}.")
            print("Empate")
        elif self.persona == "papel" and maquina == "piedra":
            print(f"El humano sacó {self.persona} la máquina sacó {maquina}.")
            print("Tú ganas")
        elif self.persona == "papel" and maquina == "tijera":
            print(f"El humano sacó {self.persona} la máquina sacó {maquina}.")
            print("Yo gano")
        elif self.persona == "piedra" and maquina == "piedra":
            print(f"El humano sacó {self.persona} la máquina sacó {maquina}.")
            print("empate")
        elif self.persona == "piedra" and maquina == "papel":
            print(f"El humano sacó {self.persona} la máquina sacó {maquina}.")
            print("yo gano")
        elif self.persona == "piedra" and maquina == "tijera":
            print(f"El humano sacó {self.persona} la máquina sacó {maquina}.")
            print("Tú ganas")
        elif self.persona == "tijera" and maquina == "piedra":
            print(f"El humano sacó {self.persona} la máquina sacó {maquina}.")
            print("yo gano")
        elif self.persona == "tijera" and maquina == "papel":
            print(f"El humano sacó {self.persona} la máquina sacó {maquina}.")
            print("Tú ganas")
        elif self.persona == "tijera" and maquina == "tijera":
            print(f"El humano sacó {self.persona} la máquina sacó {maquina}.")
            print("Empeta")
    
    def a_jugar(self):
        while True:
            seguir = input("Marca 1 para jugar y cualquier otra cosa para terminar\n")
            if seguir == "1":
                partida.elegir_jugada()
                partida.jugada()
            else:
                print("Gracias por jugar")
                break

partida = Juego()
partida.a_jugar()