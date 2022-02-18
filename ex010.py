# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

# Considere US$ 1,00 = R$ 3,27

print('='*10, ' DESAFIO 010 - Proposto ', '='*10)

carteira = float(input('Quanto você tem na carteira? R$ '))
usd = float(input('Digite o valor do dolar hoje: USD$ '))
eur = float(input('Digite o valor do euro: EUR$ '))
dolar = carteira / usd
euro = carteira / eur

print('Com R$ {:.2f} reais, você pode comprar USD$ {:.2f} dolares.'.format(carteira, dolar))
print('Com R$ {:.2f} reais, você pode comprar EUR$ {:.2f} euros.'.format(carteira, euro))

# print('='*10, ' DESAFIO 010 - Resolução - Aula 07 ', '='*10)

# real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
# dolar = real / 3.27
# print('Com R$ {:.2f} você pode comprar US$ {:.2f}.'.format(real, dolar))