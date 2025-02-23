# coding: latin1
# Tenemos un termostato inteligente que envía el valor entero decimal, en grados centígrados de la temperatura a nuestra función de Python y espera un valor de retorno.
# Debe realizar una función Python llamada "ajuste" que reciba como parámetro la temperatura, en un parámetro llamado temperatura. 
# Deberá devolver el valor False, True o None:

# False enciende el aire acondicionado y apaga la calefacción.
# True enciende la calefacción y apaga el aire acondicionado.
# None apaga ambos equipos.
 
# Si la temperatura es mayor a 27º, debe encender el aire acondicionado.
# Si la temperatura es menor a 19º, debe encender la calefacción.
# Entre 19 y 27 grados (ambos incluidos) ambos equipos deben estar apagados.

def ajuste(temperatura):

  if temperatura > 27:
    return False  # Encender aire acondicionado
  elif temperatura < 19:
    return True   # Encender calefacción
  else:
    return None  # Apagar ambos

# Ejemplo de uso:
temperatura_actual = 25
resultado = ajuste(temperatura_actual)

if resultado is True:
  print("Encender calefacción")
elif resultado is False:
  print("Encender aire acondicionado")
else:
  print("Apagar ambos equipos")


  # El mejor para mi
  # coding: latin1
def ajuste(temperatura):
    if temperatura > 27:
        print("Aire acondicionado encendido. Calefacción apagada")
        return False
    elif temperatura < 19:
        print("Calefacción encendida. Aire acondicionado apagado")
        return True   
    else:
        print("Aire acondicionado y calefacción apagados.")
        return None
        
ajuste(20)