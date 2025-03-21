'''Ejercicio 11: Gestión de cuentas bancarias
Crea una clase CuentaBancaria con atributos para titular y saldo.
Añade métodos para depositar, retirar y consultar el saldo. Usa el manejo de excepciones para evitar saldos negativos.'''
class CuentaBancaria():
    
    def __init__(self,titular,saldo):
        self.titular = titular 
        self.saldo = saldo
        
    def deposito(self):
        cantidad = float(input("Introduzca la cantidada a depositar: "))
        