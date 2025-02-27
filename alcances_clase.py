import math

class Lanzamiento():
    gravedad=9.81
    angulo=int()
    velocidad=int()
    angulo_rad=math.radians(angulo)
   
    def __init__(self, alcance, altura_max):
        self.alcance=(velocidad**2)*math.sin(2*angulo_rad)/gravedad
        self.altura_max=(velocidad**2)*(math.sin(angulo_rad))**2/(2*gravedad)  
   
    def setter(self):
        angle=int(input("Introduce el valor del ángulo de lanzamiento:  "))
        self.angulo=angle
        
    def veloz(self):
        speed=int(input("Introduce la velocidad del proyectil:  "))
        self.velocidad=speed
        
    def resultados(self, alcance, altura_max):
    
        while True:

            print(f"El alcance máximo del proyectil a {angulo} grados es de: {round(alcance,3)} metros.")
            print(f"La altura máxima del proyectil  a {angulo} grados es de:  {round(altura_max,3)} metros.")
    
lanzamiento1=Lanzamiento()
lanzamiento1.setter()
lanzamiento1.veloz()  
lanzamiento1.resultados()


'''
Se creará la clase "Lanzamiento" y tendrá varios métodos:

Método para establecer el ángulo de lanzamiento ("setter")
Método para establecer la velocidad
Para los dos datos anteriores también hacer métodos para consultar el valor ("gettters")
La gravedad es una variable que va en el código (ej. gravedad = 9.81)
Un método que realice el cálculo del alcance y la altura máxima y nos imprima por pantalla los resultados
'''