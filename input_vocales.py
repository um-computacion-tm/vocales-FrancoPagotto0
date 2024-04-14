from vocales import contar_vocales

while True:
    palabra = input('Ingrese palabra o escriba "salir" para terminar : ')
    if palabra.lower() == 'salir':
        break
    print(contar_vocales(palabra))