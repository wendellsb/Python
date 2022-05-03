from functools import total_ordering


casa = float(input('Valor da casa: '))
salario = float(input('Salario do comprador: '))
anos = float(input('Anos para pagamento: '))

parcela =  casa / (anos*12)
prestacao = salario * 0.30

if (parcela < prestacao) :
    print('Emprestimo aprovado, valor da mensalidade: {:.2f}' .format(parcela))
else :
    print('Reprovado valor da parcela ficou em: {:.2f}' .format(parcela))