import pymongo

cliente = pymongo.MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin") 

db = cliente["practica_7"] 
productos = db["productos"] 

productos = db["productos"]

productos.update_one({"nombre":"Laptop"},{"$set":{"precio":1300}}) #actualizamos el precio de los documentos con "nombre" "Laptop" a 1300.

print(productos.find_one({"nombre":"Laptop"})) #imprimimos la consulta del documento "Laptop"