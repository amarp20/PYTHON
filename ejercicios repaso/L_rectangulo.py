'''Ejercicio 13: Rectángulo
Crea una clase Rectangulo con atributos para ancho y alto.
Incluye métodos para calcular el área y el perímetro, usando un constructor para inicializar los valores.'''

class Rectangulo():

    def __init__(self, lado_menor, lado_mayor):
        self.lado_menor = lado_menor
        self.lado_mayor = lado_mayor

    def area(self):
        print(f"El área es {self.lado_mayor * self.lado_menor}")
    
    def perimetro(self):
        print(f"El perímetro es {self.lado_mayor + self.lado_menor * 2}")
    
shape1 = Rectangulo(34,98)
shape1.area()
shape1.perimetro()
shape2 = Rectangulo(12,45)
shape2.area()
shape2.perimetro()  
shape3 = Rectangulo(120,76)
shape3.area()
shape3.perimetro()