"""
Desafio 020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""
print('='*10, ' DESAFIO 020 - Proposto - Aula 08', '='*10)
from random import shuffle
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem de apresentação será: {}.'.format(lista))

print('='*30)

print('='*10, ' DESAFIO 020 - Resolução - Aula 08', '='*10)
import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: {}.'.format(lista))
