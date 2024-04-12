
 
def contar_vocales(mi_string):
    mi_string = mi_string.lower()
    vocales = ("a" ,"e","i","o","u")
    resultado = {}
    for letra in mi_string:
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] += 1
    return resultado        

