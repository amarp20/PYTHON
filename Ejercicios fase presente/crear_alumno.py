'''
Crea una clase "Alumno" en la que todos tengan:
    -Nombre
    -Apellidos
    -Edad
Crea los setter y getter de esos atributos.
Crea un método que me diga si el alumno es mayor de edad
'''

class Alumno:
    
    def __init__(self, Nombre, Apellidos, Edad):
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.Edad = Edad
        
    def get_Edad(self):
        return self.Edad
    
    def get_Nombre(self):
        return self.Nombre
    
    def get_Apellidos(self):
        return self.Apellidos
    
    def set_Edad(self, Edad):
        self.Edad = Edad
        
    def set_Nombre(self, Nombre):
        self.Nombre = Nombre
        
    def set_Apellidos(self, Apellidos):
        self.Apellidos = Apellidos
        
    def calculo_edad(self):
        
        if self.Edad >= 18:
            print(f"El alumno {self.Nombre} es mayor de edad.")
        else:
            print(f"El alumno {self.Nombre} no es mayor de edad.")
        
        
        
Alumno1 = Alumno("Manolo", "Pérez Martín", 20)
Alumno2 = Alumno("Ramón", "Bilbao", 16)
Alumno1.calculo_edad()
Alumno2.calculo_edad()


        