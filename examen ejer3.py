# coding: latin1
# Tenemos un dep�sito de agua con una capacidad total de 1800 litros, que est� conectado a una bomba de agua para su relleno. 
# La bomba de agua env�a 90 litros por minuto.
# Tenemos un medidor del dep�sito, que nos indica exactamente cuantos litros de agua nos quedan en el dep�sito.

# Debe realizar una funci�n llamada "llenado".
# Esta funci�n recibe como par�metro los litros de agua que quedan en el dep�sito, el par�metro se llamar� litros.
# La funci�n devolver� un entero, que marca el tiempo en segundos que debe estar encendida la bomba, para llenar el dep�sito.
# El llenado del dep�sito nunca debe provocar un desbordamiento.
# El llenado del dep�sito nunca debe tener una diferencia mayor a 1,5 litros con respecto a la capacidad total.
# No se permite utilizar instrucciones for ni while dentro de la funci�n.
 
# Una vez tenga realizada la funci�n, debe llamar a la misma para los siguientes valores del medidor:
# 1648
# 1696
# 1780
#coding:latin1
def llenado(litros, contador=-1):
    contador+=1
    lleno=1800
    resto=1800-litros
    tiempo=int(contador*60+resto*(6/9))

    if litros >=1710:
        print("La bomba funcionará durante ", tiempo , "segundos para completar el llenado.")
    else:
        litros=litros+90
        return llenado(litros, contador)

llenado(1440)