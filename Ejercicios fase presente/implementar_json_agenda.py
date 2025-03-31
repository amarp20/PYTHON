import json

# Abrir el archivo JSON y cargar los datos existentes
with open("recursos/contactos_lista.json", "r") as contactos:
    datos = json.load(contactos)

# Asegúrate de que el diccionario tiene una clave que contiene la lista
if "contactos" in datos and isinstance(datos["contactos"], list):
    # Añadir el nuevo contacto a la lista dentro del diccionario
    datos["contactos"].append({
        "nombre": "Paco",
        "apellidos": "diaz bancada",
        "DNI": "363456756l",
        "email": "erfhyfuiygj@gmail.com",
        "militar": True
    })

    # Guardar los cambios en el archivo JSON
    with open("recursos/contactos_lista.json", "w") as contactos:
        json.dump(datos, contactos, indent=4, ensure_ascii=False)

    print("Contacto añadido exitosamente.")
else:
    print("El archivo JSON no contiene una clave 'contactos' con una lista válida.")