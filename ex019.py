"""
Desafio 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
from random import choice
print('='*10, ' DESAFIO 019 - Proposto - Aula 08', '='*10)
nome1 = str(input('Digite o nome de um aluno: '))
nome2 = str(input('Digite o nome do outro aluno: '))
nome3 = str(input('Digite o nome de outro aluno: '))
nome4 = str(input('Digite o nome de outro aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('O nome escolhido foi: {}.'.format(escolhido))

print('='*30)

print('='*10, ' DESAFIO 019 - Resolução - Aula 08', '='*10)
import random
print('='*10, ' DESAFIO 019 - Proposto - Aula 08', '='*10)
nome1 = str(input('Digite o nome de um aluno: '))
nome2 = str(input('Digite o nome do outro aluno: '))
nome3 = str(input('Digite o nome de outro aluno: '))
nome4 = str(input('Digite o nome de outro aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O nome escolhido foi: {}.'.format(escolhido))