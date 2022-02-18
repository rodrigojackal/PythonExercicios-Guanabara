# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

print('='*10, ' DESAFIO 007 - Proposto ', '='*10)

nota1 = float(input('Digite a nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
soma = nota1 + nota2
media = soma / 2

print('A média entre a primeira nota {} e a segunda nota {} é: {:.1f}'.format(nota1, nota2, media))

#print('='*10, ' DESAFIO 007 - Resolução - Aula 07', '='*10)

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A média entre a primeira nota {} e a segunda nota {} é: {:.1f}'.format(n1, n2, m))