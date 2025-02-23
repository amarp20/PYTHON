bloques=int(input("cuantos bloques tiene?:   "))
bloques_por_fila=1
contador_de_saltos=0
while bloques >= bloques_por_fila:
    bloques=bloques-bloques_por_fila
    bloques_por_fila+=1
    contador_de_saltos+=1
    print("bloques restantes:   ", bloques)
else:
    print("Numero de filas que podras completar:   ", contador_de_saltos)