# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

print('='*10, ' DESAFIO 005 - Proposto ', '='*10)

n1 = int(input('Digite um valor: '))
suc = n1 + 1
ant = n1 - 1

print('O número antecessor de {} é {} e o número sucessor é {}'.format(n1, ant, suc))

#print('='*10, ' DESAFIO 005 - Resolução - Aula 07 ', '='*10)
# Caso não precise utilizar as váriaveis mais para frente, pode ser simplificado

n1 = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n1, (n1 - 1), (n1 + 1)))
