ano=int(input("Introduce un ano: "))
mes=str(input("Introduce un mes: "))

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

if mes or ano is None:
    print("el mes o el ano introducido no es valido")

if mes == "enero" or "marzo" or "mayo" or "julio" or "agosto" or "octubre" or "diciembre":
    print("Ese mes tiene 31 dias.")

elif mes == "abril" or "junio" or "septiembre" or "noviembre":
    print ("Ese mes tiene 30 dias.")

elif mes == "febrero" and ano is True:
    print("Ese mes tiene 29 dias.")

elif mes == "febrero" and ano is False:
    print("Ese mes tiene 28 dias.")

