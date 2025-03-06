#divisible por 4
#divisible por 400 pero no por 100
ano=int(input("Introduce un ano para saber si es bisiesto: "))
def ano_bisiesto():
    if ano is True:
        print("Este ano es bisiesto")
    else:
        print("Este ano no es bisiesto")

if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            ano=True
        else:
            ano=False
    else:
        ano=True
else:
    ano=False

ano_bisiesto()