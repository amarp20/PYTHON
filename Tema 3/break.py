grupo = [1, 2, 3, 4, 5, 6, 9]
for e in grupo:
    if e == 4:
      print("elemento invalido") #Esta es mi accion
      break
    print(e)

print("la instruccion break:")
for i in range(1, 6):
    if i == 3:
        break
    print("dentro del bucle")
print("fuera del bucle")