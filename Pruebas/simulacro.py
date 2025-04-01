'''Tenemos una empresa de gestión de residuos, que cobra por metro cúbico de basura.
Los precios cobrados son los siguientes:
Madera: 10€ m3
Plástico: 20€ m3
Hospitalarios: 40€ m3
Otros: 30€ m3
Además, el transporte cobrará a razón de 1€ por kilómetro recorrido al ir a buscar los desechos, y 1€ por m3 y kilómetro recorrido a la vuelta.
Realice una aplicación, que pregunte la cantidad de desechos de cada tipo a recoger, además de los Kilómetros y genere un presupuesto.'''

kilometros=float(input("¿Cuántos kilómetros hay hasta el punto de recogida?: "))
madera=float(input("¿Cuánta madera en kg va a entregar?: "))
plastico=float(input("¿Cuánto plástico en kg va a entregar?: "))
hospital=float(input("¿Cuánto material hospitalario en kg va a entregar?: "))
otros=float(input("¿Cuánto material de otro tipo en kg va a entregar?: "))

def presupuesto():
    print (f"El total asciende a: {(madera * 10)+(plastico * 20)+(hospital * 40)+(otros * 30)+(kilometros)+(kilometros * (madera+plastico+hospital+otros))} Euros.")

presupuesto()