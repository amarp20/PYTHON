ano=int(input("Introduce un ano para saber si es bisiesto:   "))
if ano<1588:
    print("No dentro del periodo del calendario Gregoriano")
elif ano%4!=0:
    print("Ano comun")
elif ano%100!=0:
    print("Ano bisiesto")
elif ano%400!=0:
    print("Ano comun")
else:
    print("Ano bisiesto")
