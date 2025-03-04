import random
class concurso:
    lista=[1,2,3]
    gana_sin_cambio=0
    gana_con_cambio=0
    pierde_sin_cambio=0
    pierde_con_cambio=0
    
    def __init__(self, iteraciones):
        self.iteraciones=iteraciones
    
    def concursar(self): 
        for i in range(0, self.iteraciones):
            self.lista=[1,2,3]
            jugador=random.choice(self.lista)
            premio=random.choice(self.lista)
            
            if jugador == premio:
                fase_final = []
                fase_final.append(jugador)
                self.lista.remove(jugador)
                fase_final.append(random.choice(self.lista))
            else:
                fase_final =[]
                fase_final.append(jugador)
                fase_final.append(premio)
            
            cambio = random.randint(0,1)
            
            if cambio == 0:
                fase_final.remove(jugador)
                if fase_final == premio:
                    self.pierde_sin_cambio += 1
                elif fase_final != premio:
                    self.gana_sin_cambio +=1
                    
            else:
                fase_final.remove(jugador)
                if fase_final == premio:
                    self.gana_con_cambio += 1
                elif fase_final != premio:
                    self.pierde_con_cambio +=1
    
    def informe(self):
        print(f"Cambiando la caja el jugador ha: \n -ganado el {(self.gana_con_cambio/self.iteraciones)*100}% de las veces. \n -perdido el {(self.pierde_con_cambio/self.iteraciones)*100}% de las veces. \n -no cambiando: \n -ganado el {(self.gana_sin_cambio/self.iteraciones)*100}% de las veces. \n -perdido el {(self.pierde_sin_cambio/self.iteraciones)*100}% de las veces.")
                
concurso1 = concurso(100)
concurso1.concursar()
concurso1.informe()
