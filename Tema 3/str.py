def funcion6(param1: int, param2: str):
    return param1 + param2

print(funcion6("hola", "chao"))

print("")

def funcion6(param1: int, param2: str):
    return str(param1) + param2 #comprobar que sucede su no fuerzo param1 a tipo str

print(funcion6(1, "chao"))
