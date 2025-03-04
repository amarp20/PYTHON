'''
Crea la clase "cuenta"
cada cuenta tendra un numero diferente a las demas y un saldo float
el numero de cuenta se puede consultar y modificar
pero el saldo solo puede consultarse
para modificar el saldo tenemos que hacer un ingreso o una retirada
'''
import time
class cuenta:
    saldo=float()
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo
        
    def get_numero(self):
        return self.numero
    
    def get_saldo(self):
        return self.saldo
    
    def set_numero(self, numero):
        self.numero = numero
        
    def set_saldo(self, saldo):
        self.saldo = saldo
    
    def ingreso(self):
        cantidad = float(input("Seleccione la cantidad a ingresar:  "))
        print("Operación realizada con éxito, su saldo actual es: ")
        self.saldo = cantidad + self.saldo
        print(self.saldo)
        
    def retirada(self):
        calidad = float(input("Seleccione la cantidad a retirar:  "))
        if calidad > self.saldo:
            print("No dispone de crédito suficiente para realizar esta operación, su saldo actual es: ")
            print(self.saldo)
        else:
            print("Operación realizada con éxito, su saldo actual es: ")
            self.saldo = self.saldo - calidad
            print(self.saldo)
            
    def entrada(self):
        print(f"\nBienvenido a la red de cajeros marca ACME:\nIntroduzca su tarjeta para operar.\n")
        time.sleep(5)    
        print(f"Procesando información........\n")
        time.sleep(5)
        print(f"Su número de cuenta es:\n")
        print(self.numero,"\n")
        while True:
            print(f"Seleccione una opción: \nIntroduzca 1 para consultar el saldo. \nIntroduzca 2 para ingresar divisas. \nIntroduzca 3 para retirar divisas.")
            opcion=int(input(f"Introduzca cualquier otro número para salir del programa.\n"))
            if opcion == 1:
                print(self.saldo)
            elif opcion == 2:
                self.ingreso()
            elif opcion == 3:
                self.retirada()
            else:
                print("gracias por usar la red de cajeros marca ACME")
                break

cuenta1 = cuenta(123456, 4500.23)
cuenta1.entrada()