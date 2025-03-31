import math

class Lanzamiento():

    gravedad=9.81
    
    def __init__(self, angulo, velocidad):
        self.angulo = angulo
        self.velocidad = velocidad
    
    def getter_angulo(self):
        return self.angulo
    
    def getter_velocidad(self):
        return self.velocidad
        
    def setter_angulo(self, angulo):
        self.angulo=angulo
        
    def setter_velocidad(self, velocidad):
        self.velocidad=velocidad
     
    def disparo(self):
        angulo_rad=math.radians(self.getter_angulo())
        alcance=(self.getter_velocidad()**2)*math.sin(2*angulo_rad)/self.gravedad
        altura_max=(self.getter_velocidad()**2)*(math.sin(angulo_rad))**2/(2*self.gravedad)  
        print(f"\nEl alcance máximo con ángulo {self.getter_angulo()} es de: {round(alcance, 3)} metros.")
        print(f"La altura máxima con ángulo {self.getter_angulo()} es de: {round(altura_max, 3)} metros.\n")
        
def entrada():
    angulo = None
    velocidad = None
    while True:
        print(f"\nCalculadora marca ACME \nSeleccione una opción: \nIntroduzca 1 para introducir los datos. \nIntroduzca 2 para consultar los datos. \nIntroduzca 3 para realizar el cáculo.")
        opcion=int(input(f"Introduzca cualquier otro valor para salir del programa.\n"))
        if opcion == 1:
            angulo=int(input("Introduce el valor del ángulo de lanzamiento:  "))
            velocidad=int(input("Introduce la velocidad del proyectil:  "))
        elif opcion == 2:
            if angulo is None or velocidad is None:
                print(f"\n¡¡¡POR FAVOR, INTRODUZCA PRIMERO LOS DATOS.!!!\n")
            else:
                print(f"\nEl ángulo seleccionado es {angulo} grados.\nLa velocidad seleccionada es {velocidad}m/s.\n")
        elif opcion == 3:
            if angulo is None or velocidad is None:
                print(f"\n¡¡¡POR FAVOR, INTRODUZCA PRIMERO LOS DATOS.!!!\n")
            else:
                tiro = Lanzamiento(angulo, velocidad)
                tiro.disparo()
        else:
            print("gracias por usar la calculadora de alcances marca ACME")
            break
        
entrada()
