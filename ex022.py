# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
nome=str(input('Digite seu nome completo: '))
print(nome.upper())
print(nome.lower())
nome2=(nome.split())
nome3=(''.join(nome2))
nome4=nome3.count('')
print(f'O nome {nome} tem {nome4} caracteres')

