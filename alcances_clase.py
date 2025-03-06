import math

class Lanzamiento():

    def __init__(self):
        self.angulo=None
      
    def set_angulo(self, angulo): 
        self.angulo = angulo
        
    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    def set_altura_max(self, altura_max): 
        self.altura_max = altura_max
        
    def set_alcance(self, alcance):
        self.alcance = alcance
    
    def get_angulo(self):
        return self.angulo
    
    def get_velocidad(self):
        return self.velocidad
    
    def get_alcance(self):
        return self.alcance
    
    def get_altura_max(self):
        return self.altura_max
    
    def obtener_datos(self):
        self.angulo=int(input("Introduce el valor del ángulo de lanzamiento:  "))
        self.velocidad=int(input("Introduce la velocidad del proyectil:  "))

    def calcular(self):
        angulo_rad=math.radians(self.angulo)
        self.alcance=(self.velocidad**2)*math.sin(2*angulo_rad)/9.81
        self.altura_max=(self.velocidad**2)*(math.sin(angulo_rad))**2/(2*9.81)  
    def menu(self):
        while True:
            opcion=float(input(f"Introduce una opción para:\n1 Para introducir datos.\n2 Para Comprobar datos.\n3 Para realizar cálculo.\nCualquier otro número para salir del programa.\n"))
            if opcion == 1:
                self.obtener_datos()
            elif opcion == 2:
                if self.angulo is not None:
                    print(f"La velocidad seleccionada es: {self.velocidad}m/s.\nEl ángulo seleccionado es: {self.angulo} grados.")
                else:
                    print("No hay datos introducidos, cumplimente primero la opción 1.")
            elif opcion == 3:
                if self.angulo is not None:
                    self.calcular()
                    print(f"El alcance máximo del proyectil a {self.angulo} grados es de: {round(self.alcance,3)} metros.")
                    print(f"La altura máxima del proyectil  a {self.angulo} grados es de:  {round(self.altura_max,3)} metros.")
                else:
                    print("No hay datos introducidos, cumplimente primero la opción 1.")
            else:
                print("Gracias por usar la calculadora de tiro.")
                break

lanzamiento1 = Lanzamiento()
lanzamiento1.menu()