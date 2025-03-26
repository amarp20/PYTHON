'''Ejercicio 8: Validación de contraseña
Diseña una clase Validador con un atributo para una contraseña.
Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un número.'''

class Validador:
    
    numeros = "0123456789"
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    
    def __init__(self, contrasena):
        self.contrasena = contrasena
        
    def validar(self):
        tiene_numero = any(i in self.numeros for i in self.contrasena)
        tiene_mayuscula = any(i in self.mayusculas for i in self.contrasena)
        longitud_valida = len(self.contrasena) > 7
        try:
            if tiene_numero == False:
                raise ValueError("la contraseña no tiene ningún número.")
            if tiene_mayuscula == False:
                raise ValueError("la contraseña no tiene ningún mayúsculas.")
            if longitud_valida:
                raise ValueError("la contraseña no tiene la longitud indicada.")
            print("Contraseña actualizada.")
        except ValueError as e:
            print(f"La contraseña no es válida ya que {e} ")
            
contrasena1 = Validador("Alejandro1")
contrasena2 = Validador("alejandro1")
contrasena3 = Validador("Alejandro")
contrasena4 = Validador("Al1")
contrasena1.validar()
contrasena2.validar()
contrasena3.validar()
contrasena4.validar()