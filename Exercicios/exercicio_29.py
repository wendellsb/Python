km = float(input('Informe a velocidade do carro: '))
multa = km - 80
multa *= 7

if km > 80 :
    print('Você foi multado por estar a {}km/h!'.format(km))
    print('O valor da multa total é de {} reais!'.format(multa))
    