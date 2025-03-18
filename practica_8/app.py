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
    return redirect(url_for("index"))

#Ruta para editar una persona existente
@app.route("/edit/<id>", methods=["GET", "POST"])
def edit(id):
    persona = collection.find_one({"_id": ObjectId(id)})
    if request.method == "POST":
        nuevo_nombre = request.form.get("nombre")
        collection.update_one({"_id": ObjectId(id)}, {"$set": {"nombre": nuevo_nombre}})
        return redirect(url_for("index"))
    return render_template("edit.html", persona=persona)

if __name__ == "__main__":
    app.run(debug=True) #con esto se inicia el servidor flask