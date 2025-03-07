from tabulate import tabulate as tb

tablero=[[" ","A"," ","B"," ","C"],
        ["1","_","|","_","|","_"],
        ["2","_","|","_","|","_"],
        ["3","_","|","_","|","_"]
        ]

posiciones=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]

print("Bienvenido al juego del tres en raya.")

while True:
    ficha=input("Elige tu ficha para jugar X o O: ")
    ficha_cap = ficha.upper()
    if ficha_cap == "X" or ficha_cap == "O":
        print(tb(tablero))
        posicion=input("Elige la posición de coordenadas donde quieres colocar tu ficha: ")
        posicion_cap = posicion.upper()
        if posicion_cap in posiciones:
            if posicion_cap == "A1":
                if tablero[1][1] == "_":
                    tablero[1][1] = ficha_cap
                else:
                    