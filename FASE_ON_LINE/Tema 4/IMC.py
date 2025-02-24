def pies_y_pulgadas(pies, pulgadas):
    return pies*0.3048 + pulgadas*0.0254

def libras_a_kilos(libras):
    return libras*0.4535923

def imc(peso, altura):
    if altura < 1.0 or altura > 2.5 or peso < 20 or peso > 200:
        return None
    return peso / altura ** 2

print(imc(peso=libras_a_kilos(199), altura=pies_y_pulgadas(5, 7)))
