#coding: latin1

def comprobar():
    numero=int(input("Ingrese un n�mero de tres cifras para su comprobaci�n: "))
    if numero <= 99 or numero > 999:
            print("El n�mero tiene que ser de tres cifras.")
            return comprobar()
    if numero > 99 and numero <= 999:

        centena=numero//100
        decena=(numero-centena*100)//10
        unidad=(numero-(centena*100)-(decena*10))
        valores=[centena, decena, unidad]

        if unidad == centena:
            print("Capic�a")
        if centena + unidad == decena:
            print("El centro gana.")
        if (centena+decena+unidad)%10==0:
            print("Perfecto.")
        if unidad > decena:
            valores[2], valores[1] = valores[1], valores[2]
        if decena > centena:
            valores[1], valores[0] = valores[0], valores[1]
        if valores[2] > valores[1]:
            valores[2], valores[1] = valores[1], valores[2]
        print("TOP: ", valores[0],valores[1],valores[2])


comprobar()