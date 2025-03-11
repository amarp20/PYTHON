import json
import os

class Agenda():
    
    def __init__(self, archivo="recursos/telefonos.json"): #al definir archivo pongo cual va a abrir, pero si al llamar a la clase pongo otro archivo abriría ese.
        self.archivo = archivo
        self.contactos = self.cargar_contactos() #en el constructor llamamos a la función cargar_contactos, con la que obtendremos el diccionario de telefonos.json, a partir de aquó trabajaremos con self.contactos, para al final del programa pasarlo todo a self.archivo.
    
    def cargar_contactos(self):
        if os.path.exists(self.archivo): #comprueba si la ruta del archivo entre paréntesis funciona.
            with open(self.archivo, "r") as f: #entonces ábrelo
                return json.load(f) #cárgalo y devuélveselo a self.contactos
        else:
            return {}
        
    def mostrar_agenda(self):
        if self.contactos:
            for nombre, info in self.contactos.items(): #El bucle va a recorrer las claves(nombre) y los valores(info) de self.contactos que es el diccionario que está abierto.
                print(f"\nNombre: {nombre}")
                print(f"\nTeléfono: {info['Telefono']}")
                print(f"\nEmail: {info['Email']}")
                
        else:
            print("La agenda está vacía.")
   
contacto=Agenda()
contacto.mostrar_agenda()