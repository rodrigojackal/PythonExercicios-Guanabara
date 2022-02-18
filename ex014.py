# Escreva um programa que converta uma temperatura digitada em ºC (Celsius) e converta para ºF (Fahrenheit).

c = float(input('Informe a temperatura em ºC: '))
f = (c * 1.8) + 32
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF!'.format(c, f))

# print('='*10, ' DESAFIO 014 - Resolução - Aula 07', '='*10)

c = float(input('Informe a temperatura em ºC: '))
f = 9 * c / 5 + 32
print('A temperatura de {}ºC corresponde a {}ºF!'.format(c, f))