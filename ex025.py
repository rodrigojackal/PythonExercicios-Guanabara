"""
Desafio 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""
print('='*10, ' DESAFIO 025 - Proposto / Resolução - Aula 09 ', '='*10)

nome = str(input('Qual é seu nome completo? ')).strip()

print('Seu nome tem Santos? {}'.format('SANTOS' in nome.upper()))

print('='*30)