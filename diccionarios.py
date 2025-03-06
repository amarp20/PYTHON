#se representan en pares clave:valor.
#las claves son únicas e inmutables, no se pueden repetir en el diccionario ni se pueden modificar.
'''
Hacer una aplicación para tener una agenda de teléfonos.
Crear la clase Agenda.
Los teléfonos se guardarán en un diccionario con clave: Nombre del contacto y valor: Teléfono.
Necesitamos los siguientes métodos:
    - __init__
    - Método para introducir un nuevo contacto.
    - Método para borrar un contacto (por nombre) 
    - Método para buscar un contacto (por nombre)  
    - Método para mostrar toda la agenda
'''

class Agenda():
    
    diccionario = {}
    
    def __init__(self):
        pass
    
    def getnombre(self):
        return self.nombre
    
    def getnumero(self):
        return self.numero
    
    def setnombre(self, nombre):
        self.nombre = nombre
        
    def setnumero(self, numero):
        self.numero = numero
        
    def introducir_contacto(self):
        
        nom_contacto = input("Introduzca el nombre del contacto: ")
        num_contacto = input("Introduzca el número del contacto: ")
        self.diccionario[nom_contacto] = num_contacto
        
    def eliminar_contacto(self):
        
        nom_contacto = input("Introduzca el nombre del contacto que quiere eliminar: ")
        self.diccionario.pop(nom_contacto)
        
    def buscar_contacto(self):
        nom_contacto = input("Introduzca el nombre del contacto que quiere consultar: ")
        print(self.diccionario[nom_contacto])
        
    def mostrar_agenda(self):
        print(self.diccionario)
        
    def menu(self):
        while True:
            print(f"\nAgenda de teléfonos marca ACME \nSeleccione una opción: \nIntroduzca 1 para introducir un contacto. \nIntroduzca 2 para eliminar un contacto. \nIntroduzca 3 para buscar un contacto.\nIntroduzca 4 para ver toda la agenda.")
            opcion=int(input(f"Introduzca cualquier otro valor para salir de la agenda.\n"))
            if opcion == 1:
                nuevo.introducir_contacto()
            elif opcion == 2:
                nuevo.eliminar_contacto()
            elif opcion == 3:
                nuevo.buscar_contacto()
            elif opcion == 4:
                nuevo.mostrar_agenda()
            else:
                print("gracias por usar la agenda de teléfonos marca ACME")
                break
    
nuevo = Agenda()
nuevo.menu()
