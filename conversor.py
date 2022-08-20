menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos colimbianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

def solicitud(pesos, valor_dolar):
    dolares = str(round(pesos / valor_dolar, 2))
    print ("Tienes US$:", dolares)

if opcion == 1:
    pesos = float(input("¿Cuántos pesos colombianos tienes?: "))
    solicitud(pesos, valor_dolar = 3875)
elif opcion == 2:
    pesos = float(input("¿Cuántos pesos argentinos tienes?: "))
    solicitud(pesos, valor_dolar = 175)
elif opcion == 3:
    pesos = float(input("¿Cuántos pesos mexicanos tienes?: "))
    solicitud(pesos, valor_dolar = 24)
else:
    print('Ingresa una opción válida')