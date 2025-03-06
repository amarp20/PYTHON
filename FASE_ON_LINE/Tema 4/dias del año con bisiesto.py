#coding: latin1

def bisiesto(ano, mes, dia):
    meses=["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
    if mes not in meses:
        return None
    if ano%4==0 and (ano%100!=0 or ano%400==0):
        ano_bisiesto=True
    else:
        ano_bisiesto=False
    if mes==meses[1]:
        dias=29 if ano_bisiesto else 28
    elif mes in (meses[3], meses[5], meses[8], meses[10]):
        dias=30
    else:
        dias=31
    if dia>dias or dia <=0:
        return None
    print ("Es ", dia, "de ", mes, "de", ano)

print(bisiesto(2024, "FEBRERO", 13))
