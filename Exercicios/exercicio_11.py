largura = float(input('Informe a largura: '))
altura = float(input('Informe a altura: '))
tinta = 2
area = altura * largura

print('A area é de {}m2.'.format(area))
print('Vão ser nescessarios {} litros de tinta' .format(area / tinta))