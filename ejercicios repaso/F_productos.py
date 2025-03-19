'''Ejercicio 7: Registro de productos
Crea una clase Producto con atributos para nombre, precio y cantidad en stock.
Añade un método que calcule el valor total del inventario (precio × cantidad).'''

class Producto():
    
    inventario = {
        "raton":{
        "precio":30,
        "cantidad":100},
        "teclado":{
        "precio":40,
        "cantidad":100},
        "cpu":{
        "precio":500,
        "cantidad":100}
    }
    
    def __init__(self):
        pass
    
    def precio_total(self):
        total_raton=self.inventario["raton"]["precio"] * self.inventario["raton"]["cantidad"]
        total_teclado=self.inventario["teclado"]["precio"] * self.inventario["teclado"]["cantidad"]
        total_cpu=self.inventario["cpu"]["precio"] * self.inventario["cpu"]["cantidad"]
        total = total_teclado + total_raton + total_cpu
        return total
    
valor = Producto()
print(valor.precio_total())

