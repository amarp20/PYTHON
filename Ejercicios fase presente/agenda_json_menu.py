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
            for nombre, info in self.contactos.items(): #En los diccionarios el bucle va a recorrer las claves(nombre) y los valores(info) de self.contactos que es el diccionario que está abierto.
                print(f"\nNombre: {nombre}")
                print(f"\nTeléfono: {info['Telefono']}")
                print(f"\nEmail: {info['Email']}")        
        else:
            print("La agenda está vacía.")

    def introducir_contacto(self):
        while True:
            contacto = str.upper(input("Introduzca el nombre del contacto: ")) #contacto es el pimer elemento de cada diccionario del json, en este caso el nombre del contacto
            if contacto not in self.contactos:
                num_contacto = input("Introduzca el número del contacto: ")
                email = input("Introduzca su E-mail: ")
                self.contactos[contacto] = {"Telefono": num_contacto, "Email": email} #contacto es el nombre del contacto, primer elemento de la lista. num_contacto e email se almacenan en la lista anidada dentro de contacto que son telefono e email.
                break
            else:
                print("Este nombre ya figura en tu lista de contactos, por favor elige otro nombre.")
                          
    def eliminar_contacto(self):
        contacto = str.upper(input("Introduzca el nombre del contacto que desea eliminar: "))
        if contacto in self.contactos:
            del self.contactos[contacto] #con del borramos todos los datos del contacto con el nombre elegido.
            print(f"El contacto '{contacto}' ha sido eliminado exitosamente.")
        else:
            print(f"El contacto '{contacto}' no se encuentra en la lista.")
            
    def buscar_contacto(self):
        contacto = str.upper(input("Introduzca el nombre del contacto que desea buscar: "))  
        if contacto in self.contactos:
            info = self.contactos[contacto] #la variable info van a ser los valores de la clave contacto
            print(f"Información del contacto '{contacto}':")
            print(f"Teléfono: {info['Telefono']}")
            print(f"Email: {info['Email']}")
        else:
            print(f"El contacto '{contacto}' no se encuentra en la lista.")
            
    def guardar_agenda(self): 
        with open(self.archivo, "w") as f: #esta función volverá a abrir el archivo json exterior para guardar los datos que hayamos cambiado
            json.dump(self.contactos, f, indent=4) #guardamos self.contactos que es el diccionario que estamos usando en memoria en el json
                
def menu(self):
    while True:
        print(f"\nAgenda de teléfonos marca ACME \nSeleccione una opción: \nIntroduzca 1 para introducir un contacto. \nIntroduzca 2 para eliminar un contacto. \nIntroduzca 3 para buscar un contacto.\nIntroduzca 4 para ver toda la agenda.")
        opcion=input(f"Introduzca cualquier otro valor para salir de la agenda.\n")
        if opcion == "1":
            contacto.introducir_contacto()
        elif opcion == "2":
            contacto.eliminar_contacto()
        elif opcion == "3":
            contacto.buscar_contacto()
        elif opcion == "4":
            contacto.mostrar_agenda()
        else:
            contacto.guardar_agenda()
            print("Agenda cerrada y guardada, gracias por usar la agenda de teléfonos marca ACME")
            break 
        
if __name__ == "__main__": #Esto hace que si llamo esta clase desde otro lugar no cargará este menu, ya que el menu está fuera de la clase.
    menu() 
   
contacto=Agenda()
menu()