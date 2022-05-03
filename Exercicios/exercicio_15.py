km = float(input('Informe a quantidade de KM percorrido: '))
dias = float(input('Informe a quantidade de dias de aluguel: '))
dia = dias*60
rodado = km*0.15

print('Foram percorridos: {}km' .format(km))
print('Foram {:.0f} dias de aluguel.' .format(dias))
print('Total gasto {} por dia com aluguel' .format(dia))
print('Total gasto {} por dia com kilometragem' .format(rodado))