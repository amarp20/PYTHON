# coding: latin1
# Tenemos un depósito de agua con una capacidad total de 1800 litros, que está conectado a una bomba de agua para su relleno. 
# La bomba de agua envía 90 litros por minuto.
# Tenemos un medidor del depósito, que nos indica exactamente cuantos litros de agua nos quedan en el depósito.

# Debe realizar una función llamada "llenado".
# Esta función recibe como parámetro los litros de agua que quedan en el depósito, el parámetro se llamará litros.
# La función devolverá un entero, que marca el tiempo en segundos que debe estar encendida la bomba, para llenar el depósito.
# El llenado del depósito nunca debe provocar un desbordamiento.
# El llenado del depósito nunca debe tener una diferencia mayor a 1,5 litros con respecto a la capacidad total.
# No se permite utilizar instrucciones for ni while dentro de la función.
 
# Una vez tenga realizada la función, debe llamar a la misma para los siguientes valores del medidor:
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