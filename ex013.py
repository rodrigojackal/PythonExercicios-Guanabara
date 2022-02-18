# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('='*10, ' DESAFIO 013 - Proposto ', '='*10)

salario = float(input('Digite o salário do funcionário: '))
porcentagem = int(input('Digite o valor da porcentagem que será utilizada: '))
calculo = porcentagem / 100
aumento = salario + (calculo * salario)

print('O salário atual do funcionário é R$ {} reais, porém ele ganhou uma promoção de {}% \n e passou a receber: R$ {:.2f} reais.'.format(salario, porcentagem, aumento))

# print('='*10, ' DESAFIO 013 - Resolução - Aula 07', '='*10)

salario = float(input('Qual é o salário do funcionário? R$ '))
novo = salario + (salario * 15 / 100)

print('Um funcionário que ganhava R$ {:.2f}, com 15% de aumento, passa a receber R$ {:.2f}.'.format(salario, novo))