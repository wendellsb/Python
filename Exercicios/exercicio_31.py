distancia = float(input('Informe a distancia em Km/h: '))
if distancia <= 200 :
    valor = distancia * 0.50
    print('O valor da passagem para {}km é de {:.2f} reais'.format(distancia, valor))
else :
    valor = distancia * 0.45
    print('O valor da passagem para {}km é de {:.2f} reais'.format(distancia, valor))