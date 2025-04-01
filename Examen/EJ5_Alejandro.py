'''Escribe 5 strings con frases que describan su experiencia durante el desarrollo de la asignatura.
Incluye estas frases en una lista.
Genera el código necesario, para que cada vez que se ejecute el código, muestre una frase aleatoria de esa lista.'''

import random

frase1="Incluso siendo un cabeza bote te puede encantar el python."
frase2="Para aprender un lenguaje nuevo hay que ser constante, el esfuerzo se recompensa."
frase3="Muchas veces no sabes porqué, pero funciona :)"
frase4="Cuando sientas que la cabeza te va a estallar de tanto setter and getter significa que es pincho time."
frase5="La peor experiencia fue darme cuenta que en una clase de 11 alumnos de programación solo uno sabía lo que era un d20 :("

lista=[frase1,frase2,frase3,frase4,frase5]

def mostrar_frase():
    frase = random.choice(lista)
    print(frase)
    
mostrar_frase()
mostrar_frase()
mostrar_frase()
mostrar_frase()