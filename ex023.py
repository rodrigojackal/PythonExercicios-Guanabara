"""
Desafio 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

Ex: Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1
"""
print('='*10, ' DESAFIO 023 - Proposto / Resolução - Aula 09 ', '='*10)
# Forma Numérica
num = int(input('Digite um número de 0 até 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}.'.format(num))
print('Milhar é: {}'.format(m))
print('Centena é: {}'.format(c))
print('Dezena é: {}'.format(d))
print('Unidade é: {}'.format(u))

print('='*30)
