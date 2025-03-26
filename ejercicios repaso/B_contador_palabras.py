'''Ejercicio 2: Contador de palabras
Escribe una función que reciba una cadena de texto y devuelva cuántas palabras contiene.
Luego, crea una clase Texto que use esa función como método y almacene el texto como atributo.'''

class Texto:

    def __init__(self, cadena):
        self.cadena = cadena

    def cuenta_palabras(self):

        self.cadena = self.cadena.split() #split vale para dividir un str en palabras
        return len(self.cadena)

torito = Texto("Ese toro enamorado de la Luna.")
print(torito.cuenta_palabras())



