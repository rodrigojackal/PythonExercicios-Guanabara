"""
Desafio 026: Faça um programa que leia uma frase pelo teclado e mostre:

Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.
"""
print('='*10, ' DESAFIO 026 - Proposto / Resolução - Aula 09 ', '='*10)

frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}.'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}.'.format(frase.rfind('A')+1))

# print('='*30)

# print('='*10, ' DESAFIO 026 - Resolução - Aula 09', '='*10)