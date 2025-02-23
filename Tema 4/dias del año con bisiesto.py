# coding: latin1

def bisiesto(a�o, mes, d�a):
    meses=["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
    if mes not in meses:
        return None
    if a�o%4==0 and (a�o%100!=0 or a�o%400==0):
        a�o_bisiesto=True
    else:
        a�o_bisiesto=False
    if mes==meses[1]:
        d�as=29 if a�o_bisiesto else 28
    elif mes in (meses[3], meses[5], meses[8], meses[10]):
        d�as=30
    else:
        d�as=31
    if d�a>d�as or d�a <=0:
        return None
    print ("Es ", d�a, "de ", mes, "de", a�o)

print(bisiesto(2024, "FEBRERO", 13))
