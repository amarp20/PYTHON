class Calculadora():
    
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
            
    def sumar(self):
        print(f"El resultado de {self.numero1} + {self.numero2} es: {self.numero1 + self.numero2} ")
        
    def restar(self):
        print(f"El resultado de {self.numero1} - {self.numero2} es: {self.numero1 - self.numero2} ")
        
    def multiplicar(self):
        print(f"El resultado de {self.numero1} X {self.numero2} es: {self.numero1 * self.numero2} ")
        
    def dividir(self):
        print(f"El resultado de {self.numero1} / {self.numero2} es: {self.numero1 / self.numero2} ")

