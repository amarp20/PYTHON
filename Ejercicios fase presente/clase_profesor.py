'''
va a tener (nombre{getter}, asignatura{getter y setter}, salario{numero de horas de clase x una cantidad, puede ir hardcodeado})
'''
asignaturas=["BD","HTML","PYTHON"]
class profesor():
    def __init__(self, nombre):
        self.nombre = nombre
        self.salario = float()

    def get_nombre(self):
        return self.nombre
    
    def get_asignatura(self):
        return self.asignatura
    
    def get_salario(self):
        return self.salario
    
    def set_asignatura(self, asignatura):
        self.asignatura = asignatura
        
    def set_salario(self, salario):
        self.salario = salario
        
    def asignar_asignatura(self):
        while True:
            clase=int(input(f"\nElija una opción de las siguientes para asignar una asignatura:\n1 BD\n2 HTML\n3 PYTHON\n"))
            if clase >=1 and clase <=3:
                self.asignatura = asignaturas[clase-1]
                break
            else:
                print("\nElija un número válido.")
    
    def asignar_sueldo(self):
        horas=float(input("Introduzca el número de horas impartidas: "))
        if self.asignatura == asignaturas[0]:
            self.salario= horas*60
        elif self.asignatura == asignaturas[1]:
            self.salario= horas*70
        elif self.asignatura == asignaturas[2]:
            self.salario= horas*80
   
    def mostrar_datos(self):
        print(f"El profesor {self.nombre} imparte la asignatura {self.asignatura} y tiene un salario de {self.salario}€.")
         
profesor1 = profesor("Manolo")
profesor1.asignar_asignatura()
profesor1.asignar_sueldo()
profesor1.mostrar_datos()