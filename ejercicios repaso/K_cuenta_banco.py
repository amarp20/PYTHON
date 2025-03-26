'''Ejercicio 11: Gestión de cuentas bancarias
Crea una clase CuentaBancaria con atributos para titular y saldo.
Añade métodos para depositar, retirar y consultar el saldo. Usa el manejo de excepciones para evitar saldos negativos.'''

class CuentaBancaria:
    
    def __init__(self,titular,saldo):
        self.titular = titular 
        self.saldo = saldo
        
    def deposito(self):
        cantidad = float(input("Introduzca la cantidada a depositar: "))
        self.saldo = cantidad + self.saldo
        print(f"El nuevo saldo es de {self.saldo}€.")

    def retirar(self):
        cantidad = float(input("Introduzca la cantidada a retirar: "))
        if self.saldo - cantidad >= 0:
            self.saldo = self.saldo - cantidad
            print(f"El nuevo saldo es de {self.saldo}€.")
        else:
            print(f"Operación cancelada, saldo insuficiente.\nSu saldo es de {self.saldo}€.")

    def consultar(self):
        print(f"Su saldo es de {self.saldo}€.")

    def menu(self):
        print(f"Bienvenido {self.titular}.")
        while True:
            opcion = input("Introduzca el número correspondiente a la operación que quiere realizar:\n1. Hacer un ingreso.\n2. Retirar efectivo.\n3. Consultar saldo.\nCualquier otro para salir.\n")
            if opcion == "1":
                self.deposito()
            elif opcion == "2":
                self.retirar()
            elif opcion == "3":
                self.consultar()
            else:
                print("Gracias por utilizar nuestra red de cajeros.")

consulta1 = CuentaBancaria("Manuel", 1500)
consulta1.menu()
  
        