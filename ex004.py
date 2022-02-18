# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e
# todas as informações possíveis sobre ele

print('====== DESAFIO 004 ======')

n = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaços?', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('Está em maiúsculas?', n.isupper())
print('Está em minúsculas? {}'.format(n.islower()))
print(f'Está capitalizada? {n.istitle()}')