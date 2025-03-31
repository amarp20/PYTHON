from tabulate import tabulate as tb
import random

tablero=[[" ","A"," ","B"," ","C"],
        ["1","_","|","_","|","_"],
        ["2","_","|","_","|","_"],
        ["3","_","|","_","|","_"]
        ]

x = 0
ficha_pnj = " "
posiciones=["A1","A2","A3","B1","B2","B3","C1","C2","C3"]
numeros_col = [1, 2, 3]
numeros_fil = [1, 3, 5]

print("Bienvenido al juego del tres en raya.")

def posicionar():
    posicion=input("Elige la posición de coordenadas donde quieres colocar tu ficha: ")
    posicion_cap = posicion.upper()
    if posicion_cap in posiciones:
        if posicion_cap == "A1":
            while True:
                if tablero[1][1] == "_":
                    tablero[1][1] = ficha_cap
                    break
                else:
                    print("La opción escogida no está disponible, escoja otra posición.")

        elif posicion_cap == "A2":
            while True:
                if tablero[2][1] == "_":
                    tablero[2][1] = ficha_cap
                    break
                else:
                    print("La opción escogida no está disponible, escoja otra posición.")

        elif posicion_cap == "A3":
            while True:
                if tablero[3][1] == "_":
                    tablero[3][1] = ficha_cap
                    break
                else:
                    print("La opción escogida no está disponible, escoja otra posición.")

        elif posicion_cap == "B1":
            while True:
                if tablero[1][3] == "_":
                    tablero[1][3] = ficha_cap
                    break
                else:
                    print("La opción escogida no está disponible, escoja otra posición.")

        elif posicion_cap == "B2":
            while True:
                if tablero[2][3] == "_":
                    tablero[2][3] = ficha_cap
                    break
                else:           
                    print("La opción escogida no está disponible, escoja otra posición.")

        elif posicion_cap == "B3":
            while True:
                if tablero[3][3] == "_":
                    tablero[3][3] = ficha_cap
                    break
                else:           
                    print("La opción escogida no está disponible, escoja otra posición.")

        elif posicion_cap == "C1":
            while True:
                if tablero[1][5] == "_":
                    tablero[1][5] = ficha_cap
                    break
                else:           
                    print("La opción escogida no está disponible, escoja otra posición.")

        elif posicion_cap == "C2":
            while True:
                if tablero[2][5] == "_":
                    tablero[2][5] = ficha_cap
                    break
                else:           
                    print("La opción escogida no está disponible, escoja otra posición.")

        elif posicion_cap == "C3":
            while True:
                if tablero[3][5] == "_":
                    tablero[3][5] = ficha_cap
                    break
                else:           
                    print("La opción escogida no está disponible, escoja otra posición.")
    else:
        print("la opción escogida no es válida.")

def victoria():
    global x
    if tablero[1][1] != "_" and tablero[1][1] == tablero[1][3] and tablero[1][5] == tablero[1][1]:
        x = 1
    elif tablero[2][1] != "_" and tablero[2][1] == tablero[2][3] and tablero[2][5] == tablero[2][1]:
        x = 1
    elif tablero[3][1] != "_" and tablero[3][1] == tablero[3][3] and tablero[3][5] == tablero[3][1]:
        x = 1
    elif tablero[1][1] != "_" and tablero[1][1] == tablero[2][3] and tablero[3][5] == tablero[1][1]:
        x = 1
    elif tablero[1][5] != "_" and tablero[1][5] == tablero[2][3] and tablero[1][5] == tablero[3][1]:
        x = 1
    elif tablero[1][1] != "_" and tablero[1][1] == tablero[2][1] and tablero[3][1] == tablero[1][1]:
        x = 1
    elif tablero[1][3] != "_" and tablero[1][3] == tablero[2][3] and tablero[3][3] == tablero[1][3]:
        x = 1
    elif tablero[1][5] != "_" and tablero[1][5] == tablero[2][5] and tablero[3][5] == tablero[1][5]:
        x = 1

def posicionar_pnj():
    global ficha_cap
    if ficha_cap == "X":
        ficha_pnj = "O"
    else:
        ficha_pnj = "X"
    
    while True:
        numero_c = random.choice(numeros_col)
        numero_f = random.choice(numeros_fil)
        if tablero[numero_c][numero_f] == "_":
                    tablero[numero_c][numero_f] = ficha_pnj
                    break

while True:
    ficha=input("Elige tu ficha para jugar X o O: ")
    ficha_cap = ficha.upper()
    if ficha_cap == "X" or ficha_cap == "O":
        print(f"Has elegido {ficha_cap}")
        break
    else:
        print("Opción no válida.")

while x != 1:
        print(tb(tablero))
        posicionar()
        victoria()
        if x == 1:
            ficha_ganadora=ficha_cap
            break 
        posicionar_pnj()
        victoria()
        if x == 1:
            ficha_ganadora=ficha_pnj
            break 
        
print(tb(tablero))
print(f"Fin del juego, gana {ficha_ganadora}")
    

    
                    