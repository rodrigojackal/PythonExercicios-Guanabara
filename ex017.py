"""
Desafio 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo, calcule e mostre o comprimento da hipotenusa.
"""
print('='*10, ' DESAFIO 017 - Proposto - Aula 08', '='*10)

co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hipotenusa = (ca ** 2 + co ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hipotenusa))

print('='*30)

print('='*10, ' DESAFIO 017 - Resolução - Aula 08', '='*10)
# Forma 01
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hi))

# Forma 02
import math
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(hi))

# Forma 03
from math import hypot
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}.'.format(hi))