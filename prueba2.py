#coding: latin1

def incentivo():
    if a�os>15:
        print("Su incentivo es de: ", sueldo/10, "Euros.")
    elif a�os>10:
        print("Su incentivo es de: ", sueldo/20, "Euros.")
    elif a�os>5:
        print("Su incentivo es de: ", sueldo/50, "Euros.")
    else:
        print("A usted no le corresponde incentivo.")

sueldo=int(input("Introduzca su sueldo actual: "))
a�os=int(input("Introduzca sus a�os de servicio: "))

incentivo()
