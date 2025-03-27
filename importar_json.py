import json

'''
Hay dos métodos, con este hace falta cerrar al final.
contactos=open("recursos/contactos_lista.json", "r")
datos = json.load(contactos)
print(datos)
contactos.close
'''
# Abrir el archivo en modo lectura para cargar los datos existentes este método lo cierra solo.
with open("recursos/contactos_lista.json", "r") as contactos:
    datos = json.load(contactos)  #Cuidado existe la opción loads, esta solo devuelve un string no un fichero

print(datos)

