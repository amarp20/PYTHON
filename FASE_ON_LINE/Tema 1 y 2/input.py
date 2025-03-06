print("dime lo que sea...")
anything=input()
print("Hmmm...",anything,"...en serio?")

#Despues de la funcion input sin argumento anadimos uno.

#anything=input("dime lo que sea...")
#print("Hmmm...",anything,"...en serio?")

#ahora anadimos una operacion matematica

#anything=input("ingrese un numero")
#something=anything**2.0
#print(anything,"al cuadrado es",something)
#la funcion input no esta disenada para hacer operaciones matematicas, da fallo.

#la manera de solucionarlo es con las funciones int y float.
#anything=float(input("ingrese un numero decimal..."))
#something=anything**2.0
#print(anything,"al cuadrado es",something)

anything=int(input("ingrese un numero entero..."))
something=anything**2.0
print(anything,"al cuadrado es",something)