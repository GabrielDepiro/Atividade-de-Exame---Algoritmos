print('========== Questão 03 ==========')

litros = int(input('Litros de combustível: '))

Etanol = 3,50 * litros
Gasolina = 5,25 * litros

preço = litros * Etanol
preço1 = litros * Gasolina

opção = 0
print('[1] Etanol \n[2] Gasolina')
opção = int(input('Qual é a sua opção: '))
if opção == 1:
    litros <= 5
    desconto = preço - (3,5*litros)/100
else:
    litros > 5
    desconto1 = preço - (7*litros)/100 ....
