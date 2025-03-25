'''Ejercicio 9: Promedio de notas
Crea una clase Notas con una lista de calificaciones como atributo.
Implementa un método que calcule el promedio y otro que devuelva la nota más alta. Añade manejo de excepciones para evitar notas inferiores a 0 o superiores a 10.'''

class Notas():
    
    calificaciones=[]
    
    def __init__(self, nombre ="Manolo"):
        self.nombre = nombre
    
    def meter_notas(self):
        while True:
            '''La diferencia con el otro ejercicio es que este si que impide con try la introducciones superiores a 10 e inferiores a 0, para ello  hay que tener en cuenta:
            1. Empezar el bucle con la parte que rompe, notas == -1 ya que es o no -1, no hay fallo.
            2. Seguimos con lo que no queremos que ocurra, si es mayor a 10 o menor a 0 hay un error que describo con raise ValueError.
            3. Fuera del if, con una identación menos, colocamos lo que queremos que haga si no ha saltado nada de lo anterior, self.calificaciones.append(notas).
            4. Colocamos el except con otra parte de mensaje, esto valdría en el caso de que tuviesemos diferentes errores, aquí se podría omitir.
            5. Añadimos fuera del bucle los métodos a llamar una vez roto el bucle.'''
            try:
                notas = float(input("Introduzca las calificaciones obtenidas por el alumno, pulse -1 para dejar de introducir notas.\n"))
                if notas == -1:
                    break
                if notas <= 0 or notas >= 10:
                    raise ValueError("el valor introducido no es válido.")
                self.calificaciones.append(notas)
            except ValueError as e:
                print(f"No se puede continuar ya que {e}")
                
        self.devolver_maxima()
        self.devolver_promedio()
    
    def devolver_promedio(self):
        promedio = sum(self.calificaciones)/len(self.calificaciones)
        print(f"La nota media de {self.nombre} es: {promedio}")
    
    def devolver_maxima(self):
        maxima = max(self.calificaciones)
        print(f"La nota máxima de {self.nombre} es: {maxima}")
        
alumno = Notas()
alumno.meter_notas()