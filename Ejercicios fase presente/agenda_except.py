import json
import os
import time

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
            
    def actualizar_nombre(self):
        contacto = str.upper(input("Introduzca el nombre del contacto que desea cambiar: "))  
        if contacto in self.contactos:
            nuevo_contacto = str.upper(input("Introduzca el nuevo nombre del contacto: "))  
            self.contactos[nuevo_contacto] = self.contactos.pop(contacto)
        else:
            print(f"El contacto '{contacto}' no se encuentra en la lista.")
            
    def actualizar_telefono(self):
        contacto = str.upper(input("Introduzca el nombre del contacto al que quiere cambiar el teléfono: "))  
        if contacto in self.contactos:
            nuevo_telefono = str.upper(input("Introduzca el nuevo número de teléfono: ")) 
            self.contactos[contacto] = {"Telefono":nuevo_telefono}
            print("Modificación realizada con éxito.")
        else:
            print(f"El contacto '{contacto}' no se encuentra en la lista.")
            
    def actualizar_email(self):
        contacto = str.upper(input("Introduzca el nombre del contacto al que quiere cambiar el email: "))  
        if contacto in self.contactos:
            nuevo_email = str.upper(input("Introduzca el nuevo email: ")) 
            self.contactos[contacto] = {"Email":nuevo_email}
            print("Modificación realizada con éxito.")
        else:
            print(f"El contacto '{contacto}' no se encuentra en la lista.")
            
    def modificar_datos(self):
        while True:
            print(f"\nSeleccione una opción: \nIntroduzca 1 para cambiar el nombre de un contacto. \nIntroduzca 2 para cambiar el teléfono de un contacto. \nIntroduzca 3 para cambiar el email de un contacto.")
            opcion=input(f"Si no quiere realizar más cambios introduzca cualquier otro valor para volver al menú anterior.\n")
            if opcion == "1":
                contacto.actualizar_nombre()
            elif opcion == "2":
                contacto.actualizar_telefono()
            elif opcion == "3":
                contacto.actualizar_email()
            else:
                break
            
    def guardar_agenda(self):
        try:
            with open(self.archivo, "w") as f: #esta función volverá a abrir el archivo json exterior para guardar los datos que hayamos cambiado
                json.dump(self.contactos, f, indent=4) #guardamos self.contactos que es el diccionario que estamos usando en memoria en el json
        except Exception as e:
            print(f"La agenda no se ha cerrado correctamente debido a un error de {e}.\nPodría perder los datos que no haya guardado.\nSi el problema persiste Llame al servicio de atención 666 66 66 66.")
            print("Volviendo al menú inicial............")
            time.sleep(5)
            contacto = Agenda()
            contacto.menu() 
                 
    def menu(self):
        while True:
            try:
                print(f"\nAgenda de teléfonos marca ACME \nSeleccione una opción: \nIntroduzca 1 para introducir un contacto. \nIntroduzca 2 para eliminar un contacto. \nIntroduzca 3 para buscar un contacto.\nIntroduzca 4 para ver toda la agenda.\nIntroduzca 5 para modificar un contacto.")
                opcion=input(f"Introduzca cualquier otro valor para salir de la agenda.\n")
                if opcion == "1":
                    contacto.introducir_contacto()
                elif opcion == "2":
                    contacto.eliminar_contacto()
                elif opcion == "3":
                    contacto.buscar_contacto()
                elif opcion == "4":
                    contacto.mostrar_agenda()
                elif opcion == "5":
                    contacto.modificar_datos()
                else:
                    contacto.guardar_agenda()
                    print("Agenda cerrada y guardada, gracias por usar la agenda de teléfonos marca ACME")
                    break 
            except Exception: 
                print(f"Ha ocurrido un error, vuelva a introducir una opción.") 
                
contacto = Agenda()
contacto.menu()
