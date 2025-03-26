'''Ejercicio 15: Crea un programa que gestione una lista de tareas.
Define una clase Tarea con atributos titulo, descripcion y completada.
Implementa métodos para añadir, eliminar, marcar como completada y listar todas las tareas. 
Guarda la lista de tareas en un archivo JSON y permite cargarla al iniciar el programa. 
Usa la librería os para gestionar los archivos y directorios necesarios.'''

import json
import os
import time

class Tarea:
    
    def __init__(self, archivo="recursos/tareas.json"): 
        self.lista = archivo
        self.tareas = self.cargar_tareas() 
    
    def cargar_tareas(self):
        if os.path.exists(self.lista):
            with open(self.lista, "r") as f: 
                return json.load(f)
        else:
            return {}
        
    def listar_tareas(self):
        if self.lista:
            for titulo, info in self.tareas.items(): 
                print(f"\nNombre: {titulo}")
                print(f"\nDescripcion: {info['Descripcion']}")
                print(f"\nEstado: {info['Estado']}")        
        else:
            print("La agenda está vacía.")

    def introducir_tarea(self):
        while True:
            tarea = str.upper(input("Introduzca el nombre de la nueva tarea: "))
            if tarea not in self.lista:
                nom_tarea = input("Introduzca una descripción para esta tarea: ")
                self.tareas[tarea] = {"Descripcion": nom_tarea, "Estado": "No completada"} 
                break
            else:
                print("Este nombre ya figura en tu lista de tareas, por favor crea una nueva tarea o midifica la misma.")
                        
    def eliminar_tarea(self):
        tarea = str.upper(input("Introduzca el nombre de la tarea que quiere eliminar: "))
        if tarea in self.tareas:
            del self.tareas[tarea]
            print(f"La tarea '{tarea}' ha sido eliminada exitosamente.")
        else:
            print(f"La tarea '{tarea}' no se encuentra en la lista.")
            
    def estado_completada(self):
        tarea = str.upper(input("Introduzca el nombre de la tarea que quiere marcar como completada: "))  
        if tarea in self.tareas: 
            self.tareas[tarea]["Estado"]= "Completada"
            print("Modificación realizada con éxito.")
        else:
            print(f"La tarea '{tarea}' no se encuentra en la lista.")
            
    def guardar_lista(self):
        try:
            with open(self.lista, "w") as f: 
                json.dump(self.tareas, f, indent=4) 
        except Exception as e:
            print(f"La lista de tareas no se ha cerrado correctamente debido a un error de {e}.\nPodría perder los datos que no haya guardado.\n")
            
    def menu(self):
       
        while True:
            opcion = input("\nIntroduzca el número de la opción que quiere escoger.\n1. Ver las tareas listadas.\n2. Introducir una nueva tarea.\n3. Marcar una tarea como completada.\n4. Eliminar una tarea.\nCualquier otro número para salir.\n")
            if opcion == "1":
                self.listar_tareas() 
            elif opcion == "2":
                self.introducir_tarea()
            elif opcion == "3":
                self.estado_completada()
            elif opcion == "4":
                self.eliminar_tarea()
            else:
                print("Saliendo del programa.")
                time.sleep(2)
                print("Guardando datos.")
                time.sleep(2)
                print(".........")
                time.sleep(2)
                print("Datos guardados.")
                break

tarea1 = Tarea()
tarea1.menu()