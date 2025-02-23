def es_un_triangulo(a, b, c):
    return a+b > c and b+c > a and a+c > b

def es_rectangulo(a,b,c):
    if not es_un_triangulo(a,b,c):
        return None
    if c > a and c > b:
        return c**2 == a**2 + b**2 
    if b > a and b > c:
        return b**2 == a**2 + c**2
    if a > b and a > c:
        return a**2 == b**2 + c**2

print(es_rectangulo(5,3,4))
print(es_rectangulo(3,3,3))
print(es_rectangulo(1,1,4))

