# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

print('='*10, ' DESAFIO 009 - Proposto', '='*10)

n0 = int(input('Digite um número para ver sua tabuada: '))
n1 = n0 * 1
n2 = n0 * 2
n3 = n0 * 3
n4 = n0 * 4
n5 = n0 * 5
n6 = n0 * 6
n7 = n0 * 7
n8 = n0 * 8
n9 = n0 * 9
n10 = n0 * 10

print('A tabuada do {0} é: {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}'.format(n0, n1, n2, n3, n4, n5, n6, n7, n8, n9, n10))

print('-'*12)
print('{} x 1 = {} \n{} x 2 = {} \n{} x 3 = {} \n{} x 4 = {} \n{} x 5 = {} \n{} x 6 = {} \n{} x 7 = {} \n{} x 8 = {} \n{} x 9 = {} \n{} x 10 = {}'.format(n0, n1, n0, n2, n0, n3, n0, n4, n0, n5, n0, n6, n0, n7, n0, n8, n0, n9, n0, n10))
print('-'*12)

# print('='*10, ' DESAFIO 009 - Resolução - Aula 07 ', '='*10)

num = int(input('Digite um número para ver sua tabuada: '))
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))


