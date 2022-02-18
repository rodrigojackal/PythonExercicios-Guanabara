"""
Desafio 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
"""
print('='*10, ' DESAFIO 024 - Proposto / Resolução - Aula 09 ', '='*10)

cid = str(input('Em que cidade você nasceu? ')).strip()

print(cid[:5].upper() == 'SANTO')

print('='*30)