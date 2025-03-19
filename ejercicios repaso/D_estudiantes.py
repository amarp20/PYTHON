'''Ejercicio 5: Gestión de estudiantes
Crea una clase Estudiante con atributos para nombre, edad y calificación.
Implementa métodos getter y setter, y un método que determine si el estudiante aprobó (calificación mayor o igual a 6).'''
class Estudiante():
    
    def __init__(self, nombre = "Rodrigo", edad = 18):
        self.nombre = nombre
        self.edad = edad
        
    def set_calificacion(self, calificacion):
        self.calificacion = calificacion
        
    def get_calificacion(self):
        return self.calificacion 
    
    def resultado(self):
        self.calificacion = float(input(f"Introduzaca la calificación de {self.nombre}: "))
        if self.calificacion >= 6:
            print(f"{self.nombre} ha aprobado con un {self.calificacion}")
        else:
            print(f"{self.nombre} ha suspendido con un {self.calificacion}")
            
            
estudiante1 = Estudiante("Manolo")
estudiante1.resultado()