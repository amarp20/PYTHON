'''Crea una aplicación que calcule el Índice de Masa Corporal (IMC) de una persona.
La aplicación debe pedir al usuario su peso en kilogramos y su altura en metros, y luego calcular el IMC usando la fórmula: IMC=PESOALTURA2
Debe mostrar el IMC con dos decimales.'''

import random
import time

frase1=f"\nTe veo muy bien hoy, ¿has perdido peso?.\n"
frase2=f"\nNo estás gordo, es que eres de huesos anchos.\n"
frase3=f"\nTen en cuenta que a más masa mejor se pasa.\n"
frase4=f"\nTienes una ventaja, si llegase una hambruna tienes reservas de sobra.\n"

lista=[frase1,frase2,frase3,frase4]

def menu():
    pregunta=input("Elija una opción:\nSi quiere saber su IMC pulse 1.\nSi prefiere que le demos ánimos debido a su peso pulse 2.\nCualquier otro para salir.\n")
    
    if pregunta == "1":
        print(preguntar_datos())
        
    elif pregunta == "2":
        while True:
            frase = random.choice(lista)
            print(frase)
            pregunta2=input("Elija una opción:\nSi quiere otra frase de ánimo pulse 1.\nSi prefiere volver al menú principal pulse cualquier otro.\n")
            if pregunta2 == "1":
                frase = random.choice(lista)
                print(frase)
            else:
                print("saliendo al menú inicial")
                time.sleep(2)
                print(".......")
                time.sleep(2)
                menu()
                break
    else:
        print("Esperamos que el uso de nuestra app haya sido de su agrado.")

def preguntar_datos():
    peso=float(input("Introduzca su peso: "))
    altura=float(input("Introduzca su altura: "))
    return f"Su IMC es de: {round(peso/(altura**2),2)}"
    
menu()