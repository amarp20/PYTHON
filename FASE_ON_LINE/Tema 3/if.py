largest_number=-999999999999999

while largest_number!=-1:
    number=int(input("introduce un numero, si es -1 acabara el programa y mostrara el numero mas alto:   "))
    if number > largest_number:
        largest_number=number

    if number==-1:
        print("El numero mas alto ha sido: ", largest_number)
        exit()