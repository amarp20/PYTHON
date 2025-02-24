def adding(a, b, d):
    print(a, "+", b, "+", d, "=", a+b+d)

adding(1, 2, 3)

def adding2(a, b, c):
    print(a, "+", b, "+", c, "=", a+b+c)

adding2(1, c=4, b=7)

def introduction(first_name, last_name='Gonzalez'):
    print("Hola mi nombre es", first_name, last_name)

introduction("Jorge", "Perez")
introduction("Jorge")