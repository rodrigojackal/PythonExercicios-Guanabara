# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

print('='*10, ' DESAFIO 012 - Proposto ', '='*10)

preco = int(input('Digite o preço do produto: R$ '))
porcento = int(input('Digite a porcentagem do desconto: R$ '))
calculo = porcento / 100
desconto = preco - (calculo * preco)

print('O produto custa R$ {} reais e na liquidação da loja, está com 5% de desconto \ne estará custando R$ {} reias.'.format(preco, desconto))

# print('='*10, ' DESAFIO 012 - Resolução - Aula 07 ', '='*10)

preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}.'.format(preço, novo))
