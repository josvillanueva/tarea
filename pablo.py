cuenta = float(input('introduzca el monto de la cuenta: '))
propina = float(input('introduzca el porcentaje sin signos, 10 o 15 porciento: '))

cuenta_con_propina = cuenta + (cuenta * (propina/100))

print(cuenta_con_propina)

print('esta es la cuenta total.')