#Aquí vendrá la lógica de la aplicación.
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId #Esto obtendrá los ID para identificar a las personas

app = Flask(__name__)

client = MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin")
db = client["practica_flask"]
collection = db["personas"]

#Ruta principal para mostrar lista de personas y agregar nuevas. Es el dominio principal /
@app.route("/", methods=["GET", "POST"])

def index():
    if request.method == "POST":
        nombre = request.form.get("nombre") #Aquí se accede al campo nombre del HTML y lo relacionamos con la variable nombre que estamos creando en PYTHON
        if nombre: #solo se guarda si los campos tienen valor.
            collection.insert_one({"nombre": nombre})
    
    personas = list(collection.find()) #Obtenemos la lista de personas desde MongoDB
    return render_template("index.html", personas=personas) #conectamos el personas de PYTHON con el personas del HTML

#Ruta para eliminar una persona de la base de datos
@app.route("/delete/<id>")

def delete(id):
    collection.delete_one({"_id": ObjectId(id)}) #eliminamos por ID
    return redirect(url_for("index")) #Una vez borrado vuelve a index, pero con esa persona borrada

#Ruta para editar una persona existente
@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    persona = collection.find_one({"_id": ObjectId(id)}) #Se busca a la persona por el id
    if request.method == "POST": #Método POST para lanzar información
        nuevo_nombre = request.form.get("nombre") #El nuevo nombre será el que se meta en el formulario
        collection.update_one({"_id": ObjectId(id)}, {"$set": {"nombre": nuevo_nombre}}) #Se hace la modificación
        return redirect(url_for("index")) #Después de hacer la modificación vuelve a la página index
    return render_template("edit.html", persona=persona) #Haga lo que haga abre la páginan edit donde persona es igual a persona del index

if __name__ == "__main__":
    app.run(debug=True) #con esto se inicia el servidor flask