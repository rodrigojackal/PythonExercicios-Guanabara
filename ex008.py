# Escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros

print('='*10, ' DESAFIO 008 - Proposto', '='*10)

num = int(input('Digite um distância em metros: '))
cm = num * 100
mm = num * 1000

print('O valor de metros informado foi {}, o valor em centrimestros é {} e o milimetro é {}'.format(num, cm, mm))

#print('='*10, ' DESAFIO 008 - Resolução - Aula 07', '='*10)

medida = float(input('Uma distância em metros: '))
km = medida * 0.001
hm = medida * 0.01
dam = medida * 0.1
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {} M corresponde a \n{}KM \n{}hm \n{:.1f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))
