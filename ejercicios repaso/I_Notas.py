'''Ejercicio 9: Promedio de notas
Crea una clase Notas con una lista de calificaciones como atributo.
Implementa un método que calcule el promedio y otro que devuelva la nota más alta. Añade manejo de excepciones para evitar notas inferiores a 0 o superiores a 10.'''

class Notas():
    
    calificaciones=[]
    
    def __init__(self, nombre ="Manolo"):
        self.nombre = nombre
    
    def meter_notas(self):
        try:
            notas = 0
            while notas != -1:
                notas = float(input("Introduzca las calificaciones obtenidas por el alumno, pulse -1 para dejar de introducir notas.\n"))
                if notas >= 0 and notas <= 10:
                    self.calificaciones.append(notas)
                elif notas == -1:
                    alumno.devolver_maxima()
                    alumno.devolver_promedio()
                    break
                else:
                    print("El valor introducido no es válido.")
        except Exception as e:
            print(f"Se ha producido un error del tipo {e}")
            alumno.meter_notas()
                
    def devolver_promedio(self):
        promedio = sum(self.calificaciones)/len(self.calificaciones)
        print(f"La nota media de {self.nombre} es: {promedio}")
    
    def devolver_maxima(self):
        maxima = max(self.calificaciones)
        print(f"La nota máxima de {self.nombre} es: {maxima}")
        
alumno = Notas()
alumno.meter_notas()