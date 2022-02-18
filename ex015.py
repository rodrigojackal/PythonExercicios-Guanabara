# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado

dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))
pagar = (60 * dias) + (0.15 * km)

print('O total a pagar é de {:.2f}.'.format(pagar))

# print('='*10, ' DESAFIO 015 - Resolução - Aula 07', '='*10)

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
pago = (60 * dias) + (0.15 * km)

print('O total a pagar é de {:.2f}.'.format(pago))