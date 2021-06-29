# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome?
nome=str(input('Digite seu nome completo: ')).strip()
print(f'O seu nome maisúculo é: {nome.upper()}')
print(f'O seu nome minúsculo é: {nome.lower()}')
print('O nome {} tem ao todo {} letras'.format(nome,len(nome)-nome.count(' ')))
nome2=nome.split()
# print('O nome {} tem {} letras'.format(nome2[0], nome.find(' ')))
print('O nome {} tem {} letras'.format(nome2[0], len(nome2[0])))

