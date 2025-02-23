#coding: latin1

def incentivo():
    if años>15:
        print("Su incentivo es de: ", sueldo/10, "Euros.")
    elif años>10:
        print("Su incentivo es de: ", sueldo/20, "Euros.")
    elif años>5:
        print("Su incentivo es de: ", sueldo/50, "Euros.")
    else:
        print("A usted no le corresponde incentivo.")

sueldo=int(input("Introduzca su sueldo actual: "))
años=int(input("Introduzca sus años de servicio: "))

incentivo()
