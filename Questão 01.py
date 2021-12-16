print('========== Questão 01 ==========')

salario = int(input('Digite o valor do salário: R$'))
vendas = int(input('Digite suas vendas: R$'))

c = (3*1500) / 100
n = vendas - 1500
n1 = (10*n) / 100
comissão = c + n1
final = salario + comissão

print('O salário final é {}'.format(final))
