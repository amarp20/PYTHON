import pymongo

cliente = pymongo.MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin")

db = cliente["practica_7"] 
productos = db["productos"] 

productos2 = productos.find() #como no se puede iterar una colección sobre si misma la guardamos en una variable

for producto in productos2: #por lo tanto esto es realmente una iteración de la colección producto
    print(producto)

productos3 = productos.find_one({"nombre":"raton"}) #Con este buscamos un solo tipo de producto
print(productos3)

productos.delete_one({"nombre":"raton"}) #eliminar un documento

productos.update_one({"nombre":"raton"}, {"$set": {"precio": 80}}) #actualizar un dato de un producto