# coding: latin1

def bisiesto(año, mes, día):
    meses=["ENERO", "FEBRERO", "MARZO", "ABRIL", "MAYO", "JUNIO", "JULIO", "AGOSTO", "SEPTIEMBRE", "OCTUBRE", "NOVIEMBRE", "DICIEMBRE"]
    if mes not in meses:
        return None
    if año%4==0 and (año%100!=0 or año%400==0):
        año_bisiesto=True
    else:
        año_bisiesto=False
    if mes==meses[1]:
        días=29 if año_bisiesto else 28
    elif mes in (meses[3], meses[5], meses[8], meses[10]):
        días=30
    else:
        días=31
    if día>días or día <=0:
        return None
    print ("Es ", día, "de ", mes, "de", año)

print(bisiesto(2024, "FEBRERO", 13))
