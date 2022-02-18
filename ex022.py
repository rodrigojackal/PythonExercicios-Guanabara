"""
Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome.
"""
print('='*10, ' DESAFIO 022 - Resolução - Aula 09 ', '='*10)
nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas fica: {}'.format(nome.upper()))
print('Seu nome em minúsculas fica: {}'.format(nome.lower()))
print('Seu nome tem ao todo (sem espaços): {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

print('='*30)