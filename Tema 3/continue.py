for x in range(20):
  if x%2 == 0:
    continue
  print(x)

print("\n La instruccion continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Dentro del bucle.", i)
print("fuera del bucle.")

