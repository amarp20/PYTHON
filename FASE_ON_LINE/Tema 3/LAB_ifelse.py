ingreso=float(input("caunto ingresas al ano:   "))
if ingreso<=85528:
    IPI=round((ingreso*18)/100-556.2,0)
    if IPI<=0:
        print("sus impuestos a pagar son:   0.0 Euros")
    else:
        print("sus impuestos a pagar son: ",IPI," ","Euros")
else:
    print("sus impuestos a pagar son:   ",round(((ingreso-85528)*32/100)+14839.2,0))
