"""
Desafio 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro: Ana
Último: Souza
"""
print('='*10, ' DESAFIO 027 - Proposto / Resolução - Aula 09 ', '='*10)

nc = str(input('Digite seu nome completo: ')).strip()

nome = nc.split()

print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome nome é {}'.format(nome[len(nome)-1]))

print('='*30)