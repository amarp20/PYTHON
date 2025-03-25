'''Ejercicio 8: Validación de contraseña
Diseña una clase Validador con un atributo para una contraseña.
Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un número.'''

class Validador():
    
    numeros = "0123456789"
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    mensaje1 = "Su contraseña no es válida. Ha de tener al menos un número."
    mensaje2 = "Contraseña actualizada."
    mensaje3 = "Su contraseña no es válida. Ha de tener al menos una mayúscula."
    mensaje4 = "Su contraseña no es válida. Ha de tener al ocho caracteres."
    
    def __init__(self, contrasena):
        self.contrasena = contrasena
        
    def validar(self):
        tiene_numero = any(i in self.numeros for i in self.contrasena)
        tiene_mayuscula = any(i in self.mayusculas for i in self.contrasena)
        longitud_valida = len(self.contrasena) > 7
        if tiene_numero:
            if tiene_mayuscula:
                if longitud_valida:
                    return self.mensaje2
                else:
                    return self.mensaje4
            else:
                return self.mensaje3
        else:
            return self.mensaje1 
            
contrasena1 = Validador("Alejandro1")
contrasena2 = Validador("alejandro1")
contrasena3 = Validador("Alejandro")
contrasena4 = Validador("Al1")
print(contrasena1.validar())
print(contrasena2.validar())
print(contrasena3.validar())
print(contrasena4.validar())

        

