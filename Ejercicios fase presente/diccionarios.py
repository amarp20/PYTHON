#se representan en pares clave:valor.
#las claves son únicas e inmutables, no se pueden repetir en el diccionario ni se pueden modificar.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys() 
print(x) #imprime las claves
car["color"] = "white" #añade una clave y un valor
print(x) 

y = car.values()
print(y) #imprime los valores
car["year"] = 2020 #cambia un valor
print(y) 

z = car.items()
print(z) #imprime todo el diccionario

if "model" in car: #comprobar si una clave está en el diccionario
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

print(car.get("model"))#imprime el valor de esa clave