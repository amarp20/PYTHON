'''Crea una clase Claculadora que tenga métodos para sumar, restar, multiplicar y dividir dos números.
Incluye un constructor que inicialice los dos números como atributos.'''

class Calculadora:
    
    def __init__(self, numero1=0, numero2=0):
        self.numero1 = numero1
        self.numero2 = numero2
        
    def elegir_numeros(self):
        self.numero1=float(input("Introduzca el primer número para operar: "))
        self.numero2=float(input("Introduzca el segundo número para operar: "))
            
    def sumar(self):
        print(f"El resultado de {self.numero1} + {self.numero2} es: {self.numero1 + self.numero2} ")
        
    def restar(self):
        print(f"El resultado de {self.numero1} - {self.numero2} es: {self.numero1 - self.numero2} ")
        
    def multiplicar(self):
        print(f"El resultado de {self.numero1} X {self.numero2} es: {self.numero1 * self.numero2} ")
        
    def dividir(self):
        print(f"El resultado de {self.numero1} / {self.numero2} es: {self.numero1 / self.numero2} ")
        
    def menu(self):
        while True:
            opcion=input("Elija el tipo de operación que desea realizar:\n1. Sumar\n2. Restar.\n3. Multiplicar.\n4. Dividir.\n")
            if opcion == "1":
                calculo.elegir_numeros()
                calculo.sumar()
            if opcion == "2":
                calculo.elegir_numeros()
                calculo.restar()
            if opcion == "3":
                calculo.elegir_numeros()
                calculo.multiplicar()
            if opcion == "4":
                calculo.elegir_numeros()
                calculo.dividir()
           
calculo = Calculadora()
calculo.menu()