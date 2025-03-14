#try es el trozo de código que quiero que pruebe
#except decide que hacer en caso de fallo
#finally introduce algo que se ejecutará independientemente de que el resto del código funcione
'''
try:
    print(10/0)
except Exception as e: #Exception da el error genérico que haya dado el programa.
    print(f"Ha ocurrido un error {e}")
    
finally:
    print(f"Esto se ejecuta siempre {e}") 
'''
def calculadora():
    
    try:
        x=int(input("Introduzca el dividendo: "))
        y=int(input("Introduzca el divisor: "))
        z=int(x/y)
        print(z)
    except InterruptedError:
        print(f"Ha ocurrido un error")
    except ArithmeticError: #hay muchos tipos de excepciones para cada tipo de error
        print(f"No se puede dividir entre cero.")
        
    except BaseException as e: 
        print(f"Ha ocurrido un error")
        
    finally:
        calculadora() 

calculadora()