def run():

    i = 0
    potencia = 0
    LIMITE = 1000 #al pasar el nombre de la variable a mayúsculas la convieto en CONSTANTE
    potencia = 2**i
    while potencia < LIMITE:
        print('2 elevado a la potencia ' + str(i) + ' es ' + str(potencia))
        i += 1
        potencia = 2**i

if __name__ == '__main__':
    run()