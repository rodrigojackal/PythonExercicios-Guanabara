"""
Desafio 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e
tangente desse ângulo.
"""
print('='*10, ' DESAFIO 018 - Proposto - Aula 08', '='*10)
from math import sin, cos, tan, radians
num = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {:.2f} tem o SENO {:.2f}.'.format(num, sin(radians(num))))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}.'.format(num, cos(radians(num))))
print('O ângulo de {:.2f} tem a TANGENTE de {:.2f}.'.format(num, tan(radians(num))))

print('='*30)

print('='*10, ' DESAFIO 018 - Resolução - Aula 08', '='*10)
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {:.2f} tem o SENO de {:.2f}.'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}.'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {:.2f} tem o TANGENTE de {:.2f}.'.format(ângulo, tangente))
