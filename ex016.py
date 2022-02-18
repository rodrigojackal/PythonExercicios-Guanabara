"""
Desafio 016: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex.: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.
"""
print('='*10, ' DESAFIO 016 - Proposto - Aula 08', '='*10)

from math import trunc
num = float(input('Digite um valor: '))
pi = trunc(num)
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, pi))

print('='*30)

print('='*10, ' DESAFIO 016 - Resolução - Aula 08', '='*10)
# tem três formas de ser feito: (1)

import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, math.trunc(num)))

# tem duas formas de ser feito: (2)

from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, trunc(num)))

# tem duas formas de ser feito: (3)

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, int(num)))