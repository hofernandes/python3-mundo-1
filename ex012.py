# Faça um programa que leia o preço de um produto e faça um programa que mostre com um desconto de 5%
numero=float(input('Digite um número: '))
print('Um descoto de 5% de R$ {:.2f} equivale a R$ {:.2f}'.format(numero,numero-numero*5/100))