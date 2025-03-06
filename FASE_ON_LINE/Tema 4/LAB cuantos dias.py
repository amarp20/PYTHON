ano=int(input("Introduce un ano: "))
mes=str.lower(input("Introduce un mes: "))
meses=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
if ano%4 == 0:
    if ano%100 == 0:
        if ano%400 == 0:
            ano=True
        else:
            ano=False
else:
    ano=False

if mes not in meses:
    print("el mes introducido no es valido")

elif mes == meses[0] or mes == meses[2] or mes == meses[4] or mes == meses[6] or mes == meses[7] or mes == meses[9] or mes == meses[11]:
    print("Ese mes tiene 31 dias.")

elif mes == meses[3] or mes == meses[5] or mes == meses[8] or mes == meses[10]:
    print ("Ese mes tiene 30 dias.")

elif mes == meses[1] and ano:
    print("Ese mes tiene 29 dias.")

elif mes == meses[1] and not ano:
    print("Ese mes tiene 28 dias.")
    
print(meses[1])

