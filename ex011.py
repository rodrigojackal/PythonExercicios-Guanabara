# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m² quadrado.

print('='*10, ' DESAFIO 011 - Proposto ', '='*10)

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura * largura
litro = 2
quantidade = litro / area

print('A altura é {} e a largura é {}, para pintar á área de {} metros será preciso {} litros de tinta.'.format(altura, largura, area, quantidade))

#print('='*10, ' DESAFIO 011 - Resolução - Aula 07', '='*10)

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {} m². \nPara pintar essa parede, você precisará de {} L de tinta.').format(larg, alt, area, tinta)

