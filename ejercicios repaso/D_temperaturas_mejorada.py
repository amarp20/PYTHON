'''Ejercicio 4: Conversor de temperaturas
Diseña una clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa.
Usa un constructor para inicializar una temperatura base.'''
class ConversorTemperartura():
    
    def __init__(self):
            pass
    
    def set_temperatura(self, temperatura):
        self.temperatura = temperatura
        
    def conv_cel_fah(self):
        self.temperatura = float(input("Introduzca la temperatura en grados Celsius: "))
        fahrenheit = (self.temperatura*1.8)+32
        return fahrenheit
        
    def conv_fah_cel(self):
        self.temperatura = float(input("Introduzca la temperatura en grados Farenheit: "))
        celsius = (self.temperatura-32)*(5/9)
        return celsius
        
    def menu(self):
        opcion=input("Introduzca un número para elegir que quiere convertir:\n1. De Celsius a Fahrenheit.\n2. De Fahrenheit a Celsius.\nCualquier otro valor para salir: ")
        while True:
            if opcion == "1":
                print(f"Son {conversion.conv_cel_fah()} grados Fahrenheit.")
            elif opcion == "2":
                print(f"Son {conversion.conv_fah_cel()} grados Celsius.")
            else:
                print("Gracias por usar el conversor de temperatura marca ACME.")
                break
                  
conversion = ConversorTemperartura()
conversion.menu()