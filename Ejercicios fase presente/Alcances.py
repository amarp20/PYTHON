import math
class disparo():
    def __init__(self):
        pass
    def alcance(self):
    
        while True:
            velocidad=int(input("Introduce la velocidad del proyectil:  "))
            angulo1=int(input("Introduce el valor mínimo del rango de ángulos de lanzamiento:  "))
            angulo2=int(input("Introduce el valor máximo del rango de ángulos de lanzamiento:  "))
            gravedad=float(input("introduce la gravedad, si quieres el valor standard de La Tierra introduce 9.81:  "))

            for i in range(angulo1, angulo2+5, 10):
                angulo_rad=math.radians(i)
                alcance=(velocidad**2)*math.sin(2*angulo_rad)/gravedad
                altura_max=(velocidad**2)*(math.sin(angulo_rad))**2/(2*gravedad)
                print(f"El alcance máximo del proyectil a {i} grados es de: {round(alcance,3)} metros.")
                print(f"La altura máxima del proyectil  a {i} grados es de:  {round(altura_max,3)} metros.")
            
alcance1=disparo()
alcance1.alcance()
