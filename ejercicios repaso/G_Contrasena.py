'''Ejercicio 8: Validación de contraseña
Diseña una clase Validador con un atributo para una contraseña.
Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un número.'''

class Validador():
    
    numeros = "0123456789"
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890"
    mensaje1 = "Su contraseña no es válida. Su longitud ha ser ser mínimo de ocho caracteres y ha de tener al menos una mayúscula y un número."
    mensaje2 = "Contraseña actualizada."
    
    def __init__(self, contrasena):
        self.contrasena = contrasena
        
    def validar(self):
        tiene_numero = any
            
contrasena1 = Validador("Alejandro1")
contrasena2 = Validador("alejandro1")
contrasena3 = Validador("Alejandro")
contrasena4 = Validador("Al1")
print(contrasena1.validar())
print(contrasena2.validar())
print(contrasena3.validar())
print(contrasena4.validar())

  def validar(self):
        # Verifica si la contraseña tiene al menos un número
        tiene_numero = any(caracter in self.numeros for caracter in self.contrasena)
        # Verifica si la contraseña tiene al menos una mayúscula
        tiene_mayuscula = any(caracter in self.mayusculas for caracter in self.contrasena)
        # Verifica si la longitud de la contraseña es mayor a 7
        longitud_valida = len(self.contrasena) > 7

        # Valida todos los requisitos
        if tiene_numero and tiene_mayuscula and longitud_valida:
            return self.mensaje2
        else:
            return self.mensaje1

