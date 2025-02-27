class militar:
    empleo=""
    nombre=""
    edad=int()
      
    def __init__(self):
       pass
 
    def saludo(self):
        print("A sus órdenes, buenos días.") 
        
    def dalenombre(self, name):
        self.nombre=name
        
    def dimenombre(self):
        print(f"El militar se llama:  {self.nombre}")
        
    def daleempleo(self, rank):
        self.empleo=rank
        
    def dimeempleo(self):
        print(f"El militar es:  {self.empleo}")
        
    def años(self, age):
        self.edad=age
        
    def dimeaños(self):
        print(f"El militar tiene {self.edad} años.")
        
    def cumpleaños(self):
        self.edad+=1
        
        
militar1=militar()
militar1.años(30)
militar1.cumpleaños()
militar1.dimeaños()



