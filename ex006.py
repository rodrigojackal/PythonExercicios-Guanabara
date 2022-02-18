# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

print('='*10, ' DESAFIO 006 - Proposto ', '='*10)

n1 = int(input('Digite um número: '))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1 ** (1/2)

print('O dobro de {} vale {}.'.format(n1, dobro))
print('O triplo de {} vale {}.'.format(n1, triplo))
print('A raíz quadrada de {} é igual a {:.2f}.'.format(n1, raiz))

#print('='*10, ' DESAFIO 006 - Resolução - Aula 07 ', '='*10)

n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n, (1/2))))
