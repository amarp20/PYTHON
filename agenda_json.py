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

    def introducir_contacto(self):
        while True:
            contacto = input("Introduzca el nombre del contacto: ")
            nom_contacto = contacto.upper()
            if nom_contacto not in self.contactos:
                num_contacto = input("Introduzca el número del contacto: ")
                email = input("Introduzca su E-mail: ")
                self.contactos[nom_contacto] = {"Telefono": num_contacto, "Email": email} 
                self.guardar_contactos()
                break
            else:
                print("Este nombre ya figura en tu lista de contactos, por favor elige otro nombre.")
                
    def guardar_contactos(self): 
        with open(self.archivo, "w") as f:
            json.dump(self.contactos, f) 

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
                print("gracias por usar la agenda de teléfonos marca ACME")
                break 
   
contacto=Agenda()
contacto.menu()