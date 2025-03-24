'''Diseña una clase AnalizadorTexto con un atributo para una cadena de texto.
Implementa un método que cuente cuántas vocales (a, e, i, o, u) hay en el texto.'''

class AnalizadorTexto():
    
    vocales = "aeiouAEIOU"
    
    def __init__(self, cadena = " "):
        self.cadena = cadena
        
    def contar_vocales(self):
        counter = 0
        for i in self.cadena:
            if i in self.vocales:
                counter +=1
        return counter
        
texto = AnalizadorTexto("Esto es una prueba")
print(texto.contar_vocales())