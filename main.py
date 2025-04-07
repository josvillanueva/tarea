print("Este es el main")


num1 = 100
num2 = 50
num3 = 25
num4 = 10

print(num1 + num2 * num3)

print((num1 + num2) * num3 - num4)

print((num1 + num2) * (num3 - num4) / (num1 - num1))

def resta(a,b):
    return a-b


cuenta = float(input('introduzca el monto de la cuenta: '))
propina = float(input('introduzca el porcentaje sin signos, 10 o 15 porciento: '))

cuenta_con_propina = cuenta + (cuenta * (propina/100))

print(cuenta_con_propina)

print('esta es la cuenta total.')
