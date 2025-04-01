'''Escribe un programa que convierta una cantidad de metros a kilómetros, centímetros y milímetros.
La función debe recibir la cantidad de metros como parámetro y devolver un diccionario con las conversiones.
Contempla validar que la entrada sea un número positivo.'''

'''def convertir(metros):
    if metros < 0:
        return "El valor introducido es negativo, no es posible ejecutar el cálculo."
    else:
        diccionario={}
        kilometros=metros/1000
        centimetros=metros*100
        milimetros=metros*1000
        diccionario["Kilometros"]=kilometros
        diccionario["Centimetros"]=centimetros
        diccionario["milimetros"]=milimetros
        return diccionario

print(convertir(50))
print(convertir(-10))'''

def convertir(metros):

    diccionario={}
    kilometros=metros/1000
    centimetros=metros*100
    milimetros=metros*1000
    diccionario["Kilometros"]=kilometros
    diccionario["Centimetros"]=centimetros
    diccionario["milimetros"]=milimetros
    return diccionario

try:
    a=float(input("Introduzca un número para convertir a kilómetros, centímetros y milímetros: "))
    if a < 0:
        raise ValueError ("Necesito un número positivo.")
    print(convertir(a))
except ValueError as e:
    print(f"Imposible calcular. {e}")
    
