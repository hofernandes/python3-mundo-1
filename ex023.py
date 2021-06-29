# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# num=str(input('Digite um número: '))
# print(f'Unidade: {num[3]}\nDezena: {num[2]}\nCentena: {num[1]}\nMilhar: {num[0]}')
num2=int(input('Digite um número: '))
print(f'Unidade: {((num2%1000)%100)%10}')
print(f'Dezena: {((num2%1000)%100)//10}')
print(f'Centena: {(num2%1000)//100}')
print(f'Milhar: {num2//1000}')

