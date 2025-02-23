def es_un_triangulo(a, b, c):
    if a+b <= c:
        return False
    if b+c <= a:
        return False
    if a+c <= b:
        return False

    return True

print(es_un_triangulo(1,1,1))
print(es_un_triangulo(1,1,3))

#mas corto

def es_un_triangulo(a, b, c):
    if a+b <= c or b+c <= a or a+c <= b:
        return False

    return True

print(es_un_triangulo(1,1,1))
print(es_un_triangulo(1,1,3))

#mas corto

def es_un_triangulo(a, b, c):
    return a+b > c and b+c > a and a+c > b

a=float(input("Ingresa la longitud del primer lado:  "))
b=float(input("Ingresa la longitud del segundo lado:  "))
c=float(input("Ingresa la longitud del tercer lado:  "))


if es_un_triangulo(a,b,c):
    print("Si, si puede ser un triangulo")
else:
    print("No, no puede ser un triangulo")