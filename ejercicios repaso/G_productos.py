'''Ejercicio 7: Registro de productos
Crea una clase Producto con atributos para nombre, precio y cantidad en stock.
Añade un método que calcule el valor total del inventario (precio × cantidad).'''

class Producto:
    
    inventario = {}
    totales = []
    
    def __init__(self, nombre, precio, cantidad):
        self.nombre=nombre
        self.precio=precio
        self.cantidad=cantidad
    
    def meter_productos(self):
        self.inventario[self.nombre]={"precio":self.precio, "cantidad": self.cantidad}
        

    def precio_total(self):
        for i in self.inventario:
            total=self.inventario[i]["precio"]*self.inventario[i]["cantidad"]
            self.totales.append(total)
        print(sum(self.totales))
            
    
cosa1 = Producto("raton",20,50)
cosa1.meter_productos()
cosa1 = Producto("teclado",30,50)
cosa1.meter_productos()
cosa1 = Producto("cpu",200,50)
cosa1.meter_productos()
cosa1 = Producto("monitor",100,50)
cosa1.meter_productos()
cosa1.precio_total()

