c0=int(input("Introduce un numero mayor a 0:   "))
counter=0
while c0 != 1:
    if c0 % 2==0:
        c0 = c0 // 2
        print("c0 ahora es:   ", c0)
        counter+=1
    elif c0 % 2 != 0:
        c0 = (3*c0)+1
        print("c0 ahora es:   ", c0)
        counter+=1
else:
    print("para llegar aqui hemos tenido que hacer los siguientes saltos:   ", counter)
