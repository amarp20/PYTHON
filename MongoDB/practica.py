import pymongo

print(pymongo.__version__) #Muestra la versión de pymongo instalada

cliente = pymongo.MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin") #marcamos la db a la que queremos conectar

db = cliente["practica_7"] #dentro de la conexión cliente creamos la db practica_7
productos = db["productos"] #dentro de la db practica_7 creame la colección nproductos

#dbs = cliente.list_database_names() #método para mostrar las bases de datos en el servidor

#documento = {"nombre": "Laptop", "precio": 1200, "stock": 5} #escribimos un documento con un producto y sus datos

#productos.insert_one(documento) #damos la instrucción de crear el documento

numero_productos = int(input("Introduzca el número de productos a meter: "))
numero_productos_metidos = 0

while numero_productos_metidos < numero_productos: #creamos un bucle para meter productos por consola
    
    nombre = input("nombre: ")
    precio = input("precio: ")
    stock = input("stock: ")
    
    producto = {"nombre": nombre, "precio": precio, "stock": stock}

    productos.insert_one(producto)
    
    numero_productos_metidos+=1


# cliente.close() #Método para cerrar la db una vez acabe el programa

