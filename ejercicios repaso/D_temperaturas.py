'''Ejercicio 4: Conversor de temperaturas
Diseña una clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa.
Usa un constructor para inicializar una temperatura base.'''

class ConversorTemperartura:
    
    def __init__(self, temperatura = 46):
            self.temperatura = temperatura
        
    def conv_cel_fah(self):
        print(f"{self.temperatura} grados Celsius son {(self.temperatura*1.8)+32} grados Fahrenheit.")
        
    def conv_fah_cel(self):
        print(f"{self.temperatura} grados Farenheit son {(self.temperatura-32)*(5/9)} grados Celsius.")
                  
conversion = ConversorTemperartura()
conversion.conv_cel_fah()
conversion.conv_fah_cel()